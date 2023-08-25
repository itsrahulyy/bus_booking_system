from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path("about",views.about, name="about"),
    path("findbus", views.findbus, name="findbus"),
    path("bookings", views.bookings, name="bookings"),
    path("bookinghistory", views.bookinghistory, name="bookinghistory"),
    path("cancel", views.cancel, name="cancel"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("success", views.success, name="success"),
    path("signout", views.signout, name="signout")
    ,

]

