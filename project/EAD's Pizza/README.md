# EAD's Pizza
#### Video Demo:  https://youtu.be/1atxI4MpTLI
#### Description:
CS50's Introduction to web application and programming was a great project
i have done in my lifetime. I aslo took web application course of cs50.
Now I have designed the web application using Python's web framework called Django. Django is a very
powerful web application frameowork. It eases the pain of rushing through the html pages.
#Introduction to web application:
.EAD's Pizza is a web based django application which lets the pizza shop owners or any other restaurant
to manage the orders of their customers or their employees as well.
The users are welcomed by a signup form in a hopmepage.
It lets users create accounts and login. Their account information gets stored in a database and their orders
are synced as well. The admin can login to the admin panel of the website and expand the menu by adding
more items to it. He or she can accept or decline the orders which gets reflected at the customer side as
well-by getting into the my orders section in customer address.
The web application has a django based user authentication in place which is secure and fast.The applicatoin
rembers users through sessions .Users can get to any page from anywhere tthrough the universal navbar which changes its contents according to the page view. I have used some functionality of bootstrap in my app which makes it mobile responsive as well. I have also taken into consideration the security part of the application. Without authentication the users can't traverse through the locked paths . They needed to be logged in as the legitimate user. The database has many tables. The tables are connected through foreign keys and they draw from each other various relations.
The customer can view the status of the order in his my orders section.
I have created admin age for the managers to manage their orders.
# How the Webpage Works?
First time user's can signup using the signup form
they can then login using login page
they can order the selected no of pizzas and pizza types.
Get the status of the ordered items.
View the orders and order status in my orders page
# How the backend is created?
only admin can login using admin credentials.
he can add to menu various pizza at the home page.
He can update the status of customer order by going into orders page of admin
He can accept or reject the order.
## Routing
Each route checks if the user is authenticated. It means if correct mail and password were supplied and what role it has.
## Sessions
The webpage uses sessions to confirm that user is registered. Once the user logins, his credentials are checked

###### So User's enjoy the web application, manage your orders and take your restaurant for a ride up.