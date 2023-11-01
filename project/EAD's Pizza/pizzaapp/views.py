from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomerModel, OrderModel, PizzaModel
from django.contrib.auth.models import User

# Create your views here.
def adminloginview(request):
    return render(request,"pizzaapp/adminlogin.html")
def authenticateadmin(request):
    username= request.POST['username']
    password= request.POST['password']
##authentication of the user
    user = authenticate(username= username, password = password)
    #user exists
    if user is not None and user.username=='admin':
        login(request,user)
        return redirect('adminhomepage')
    #user doesn't exists
    if user is None or user.username != 'admin':
        messages.add_message(request,messages.ERROR, "Invalid Credentials")
        return redirect('adminloginpage')

def adminhomepageview(request):
    if not request.user.is_authenticated:
        return redirect("adminloginpage")
    context = {'pizzas':PizzaModel.objects.all()}
    return render(request,"pizzaapp/adminhomepage.html",context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addpizza(request):
    pizza = request.POST['pizza']
    price = request.POST['price']
    PizzaModel(name = pizza, price= price).save()
    return redirect('adminhomepage')

def deletepizza(request,pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')
def homepageview(request):
    return render(request,'pizzaapp/homepage.html')

def signupuser(request):
    username=request.POST['username']
    password=request.POST['password']
    phone=request.POST['phone']
    fname=request.POST['fname']
    #check if user exist already
    if User.objects.filter(username=username).exists():
        messages.add_message(request,messages.ERROR,"User Already exists")
        return redirect('homepage')

    #signup the user
    User.objects.create_user(username=username, password = password ,first_name=fname).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(userid=User.objects.all()[int(lastobject)].id, phone= phone).save()
    messages.add_message(request,messages.ERROR,"User Successfully Created")
    return redirect("homepage")
def userloginview(request):
    return render(request,"pizzaapp/userlogin.html")

def customerauthenticate(request):
    username=request.POST['username']
    password=request.POST['password']
    user = authenticate(username= username, password = password)
    #user exists
    if user is not None :
        login(request,user)
        return redirect('customerhomepage')
    #user doesn't exists
    if user is None:
        messages.add_message(request,messages.ERROR, "Invalid Credentials")
        return redirect('userloginpage')

def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect("userloginpage")
    username= request.user.username
    context={'username':username,'pizzas':PizzaModel.objects.all()}
    return render(request,'pizzaapp/customerhomepage.html',context)

def userlogout(request):
       logout(request)
       return redirect("userloginpage")

def placeorder(request):
    if not request.user.is_authenticated:
        return redirect("userloginpage")
    username = request.user.username
    phone = CustomerModel.objects.filter(userid=request.user.id)[0].phone
    address = request.POST['address']
    ordereditems = ""
    for pizza in PizzaModel.objects.all():
        pizzaid= pizza.id
        name = pizza.name
        price = pizza.price
        quantity = request.POST.get(str(pizzaid)," ")
        if str(quantity) != "0" and str(quantity) != " " and int(len(address)) > 4:
            ordereditems = ordereditems + name + ":- "+ "Price: " +str(int(quantity)*int(price)) + " " + "quantity: " + quantity + "; "
    
    if ordereditems != "":
        OrderModel(username = username, phone = phone, address= address,ordereditems = ordereditems ).save()
        messages.add_message(request,messages.SUCCESS,"Order Successfully Placed")
    else:
        messages.add_message(request,messages.ERROR,"Please Add Quantity Or Enter an Adress!")
    return redirect('customerhomepage')

def userorders(request):
    orders = reversed(OrderModel.objects.filter(username=request.user.username))
    username=request.user.username
    context = {'orders':orders, 'name':username}
    return render(request, "pizzaapp/userorders.html",context)        

def adminorders(request):
    if not request.user.is_authenticated:
        return redirect("adminloginpage")
    orders = reversed(OrderModel.objects.all())
    context = {"orders":orders}
    return render(request, "pizzaapp/adminorders.html",context)   
    
def acceptorder(request,orderpk):
    if not request.user.is_authenticated:
        return redirect("adminloginpage")
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status = "accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])
def declineorder(request,orderpk):
    if not request.user.is_authenticated:
        return redirect("adminloginpage")
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status = "declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])