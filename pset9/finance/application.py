import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    #current cash with the user;
    current_cash = db.execute("SELECT cash from users where id =:uid", uid = session["user_id"])
    balance = current_cash[0]["cash"]

    # getting stocks related info;
    portfolio = db.execute("SELECT symbol as Symbol, SUM(no_shares) as Shares from transactions where u_id =:uid GROUP BY symbol", uid = session["user_id"])
    shares = []
    value = 0
    for stock in portfolio:
        if stock.get("Shares") == 0:
            continue
        symbol = lookup(stock.get("Symbol"))
        price = symbol.get("price")
        no_shares = stock.get("Shares")
        total = price * no_shares
        stock["Price"] = usd(price)
        stock["Total"] = usd(total)
        shares.append(stock)
        value += round(total,2)
    grand_total = value + balance

    # rneder template
    return render_template("index.html", value = usd(value), shares = shares, balance = usd(balance), grand_total = usd(grand_total))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if request.form.get("symbol"):
            share = lookup(request.form.get("symbol").upper())
        else:
            return apology("please enter stock symbol", 400)

        # checking for valid symbol
        if share == None:
            return apology("Enter Valid Symbol", 400)
        #Validating shares no
        shares = request.form.get("shares")
        if not shares or not shares.isdigit():
            return apology("Enter the Valid No of shares", 400)
        if int(shares) < 1:
            return apology("Enter positive number", 400)

        #getting variables
        symbol = share.get("symbol")
        price = share.get("price")
        no_shares = int(shares)
        total = price * no_shares
        #checking balance of user:
        cash = db.execute("select cash from users where id = ?", session["user_id"])
        balance = cash[0]['cash']
        new_balance = balance - total
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #set order
        if balance >= total:
            db.execute("INSERT into transactions (u_id, symbol, price, no_shares, total, timestamp) VALUES(?,?,?,?,?,?)", session['user_id'],symbol,price,no_shares,total,timestamp)
            #update cash in user database
            db.execute("UPDATE users SET cash = :cash where id = :uid", cash = new_balance, uid = session["user_id"])
            flash("Transaction Successfull")
            return redirect("/")
        else:
            return apology("Not enough money")








    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("SELECT symbol as symbol, no_shares as no_shares, price as price, timestamp as timestamp from transactions where u_id=:uid", uid = session["user_id"])
    return render_template('history.html', history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if request.form.get("symbol"):
            quote = lookup(request.form.get("symbol").upper())
        else:
            return apology("Please enter Symbol",400)
        if quote == None:
            return apology("Please Enter Valid Symbol", 400)
        else:
            symbol = quote.get("symbol")
            price = quote.get("price")
            return render_template("quoted.html", symbol = symbol, price = usd(price))





    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear() #forget old userids
    #logic for post method in register.html
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Must provide username", 400)
        elif not request.form.get("password"):
            return apology("Must provide password", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match", 400)
            # check duplicacy of username
        elif len(db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))) == 0:
            hash = generate_password_hash(request.form.get("password"))
            user_id = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username = request.form.get("username"), hash = hash )
             # remember user
            session["user_id"] = user_id
            flash("Registered successfully!")
            return redirect("/")

        else:
            return apology("Username already exists!")


#check for get method
    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    #db request
    rows = db.execute("SELECT symbol as symbol, SUM(no_shares) as no_shares from transactions where u_id=:uid order by symbol",uid=session["user_id"])
    if request.method == "POST":
        shares = request.form.get("shares")
        symbol = request.form.get("symbol")

        if symbol:
            #get the no of shares to sell for the symbol;
            sell_shares = db.execute(
                    "SELECT SUM(no_shares) as no_shares from transactions where u_id=:uid AND symbol=:symbol", uid=session["user_id"], symbol=symbol)
            no_shares_sell = sell_shares[0]["no_shares"]
        else:
            return apology("Please Choose Stock Symbol", 000)
        if not shares or not shares.isdigit() or not int(shares) >= 1:
            return apology("Please enter valid no of shares", 999)
        elif int(shares) <= no_shares_sell:
            cash = db.execute("SELECT cash from users where id=:uid",uid=session['user_id'])
            cash = cash[0]["cash"]
            stock = lookup(symbol)
            price = stock.get("price")
            total = int(shares) * price
            new_cash = cash + total
            shares = int(shares)

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            #Updating cash in user's account
            db.execute("UPDATE users SET cash=:new_cash where id=:uid", new_cash = round(new_cash,2), uid = session["user_id"])
            # updating transactions table;
            db.execute("INSERT INTO transactions (u_id,symbol, price, no_shares, total, timestamp) VALUES (?,?,?,?,?,?)",
            session["user_id"], symbol, price, -shares, total, timestamp )
            # on successfull
            flash("Successfully sold!")
            return redirect("/")
        else:
            return apology("Not enough shares to Sell!!", 400)
    else:
        symbols = []
        for stock in rows:
            symbols.append(stock.get("symbol"))
        return render_template("sell.html", symbols=symbols)

# change password
@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        if not request.form.get("password"):
            return apology("please provide password!!", 888)
        elif request.form.get("password") != request.form.get("confirm"):
            return apology("Passwords don't match")
        else:
            psswd_hash = generate_password_hash(request.form.get("password"))
            db.execute("UPDATE users SET hash =:pwd_hash where id = :uid",pwd_hash=psswd_hash,uid=session["user_id"])
            flash("Password Changed Successfully")
            return redirect("/")
    else:
        return render_template("change_password.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
