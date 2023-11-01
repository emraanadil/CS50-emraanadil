from django.contrib import admin
from django.urls import path
from .views import acceptorder, addpizza, adminloginview,adminhomepageview, adminorders, authenticateadmin, customerauthenticate, customerwelcomeview, declineorder, deletepizza, homepageview, logoutadmin, placeorder, signupuser, userloginview, userlogout, userorders

urlpatterns = [
    path('admin/',adminloginview,name="adminloginpage"),
    path('authenticateadmin/',authenticateadmin,name="authenticateadmin"),
    path('admin/homepage/',adminhomepageview,name="adminhomepage"),
    path('adminlogout/',logoutadmin),
    path('addpizza/',addpizza),
    path("deletepizza/<int:pizzapk>/",deletepizza),
    path('',homepageview,name='homepage'),
    path('signupuser/',signupuser),
    path('loginuser.html/',userloginview , name="userloginpage"),
    path('customer/authenticate/',customerauthenticate),
    path('customer/welcome/',customerwelcomeview,name="customerhomepage"),
    path('userlogout/',userlogout),
    path("placeorder/",placeorder),
    path("userorders/",userorders),
    path('adminorders/',adminorders),
    path('acceptorder/<int:orderpk>/',acceptorder),
    path('declineorder/<int:orderpk>/',declineorder)
]
