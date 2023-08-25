from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bus,User,Book
from decimal import Decimal
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def about(request):
    return render(request,'myapp/about.html')

@login_required(login_url='signin')
def findbus(request):
    context={}
    if request.method=='POST':
        source_r=request.POST.get('source')
        dest_r=request.POST.get('destination')
        date_r=request.POST.get('date')

        bus_list=Bus.objects.filter(source=source_r,dest=dest_r,date=date_r)
        if bus_list:
            return  render(request,'myapp/list.html', locals())
        else:
            context["error"]="Sorry no bus available on the date"
            return render(request,'myapp/findbus.html', context)
    else:
        return render(request, 'myapp/findbus.html')

@login_required(login_url='signin')
def bookings(request):
    context={}
    if request.method=='POST':
        id_r=request.POST.get('bus_id')
        seats_r=int(request.POST.get('no_seats'))

        bus=Bus.objects.get(id=id_r)
        if bus:
            if bus.rem > int(seats_r):
                name_r=bus.bus_name
                cost=int(seats_r)* bus.price
                source_r=bus.source
                dest_r=bus.dest
                nos_r=Decimal(bus.nos)
                price_r=bus.price
                date_r=bus.date
                time_r=bus.time
                username_r=request.user.username
                email_r=request.user.email
                userid_r=request.user.id
                rem_r=bus.rem - seats_r
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book=Book.objects.create(name=username_r,email=email_r,userid=userid_r,
                                         bus_name=name_r,source=source_r,busid=id_r,
                                         dest=dest_r,price=price_r,nos=seats_r,
                                         date=date_r,time=time_r,status='BOOKED')
                print(book.id)
                return  render(request,'myapp/bookings.html',locals())
            else:
                context['error']="sorry, only few ticktes are available"
                return render(request,'myapp/findbus.html', context)

    else:
        return render(request, 'myapp/findbus.html')

@login_required(login_url='signin')
def bookinghistory(request, new={}):
    context={}
    id_r=request.user.id
    book_list=Book.objects.filter(userid=id_r)

    if book_list:
        return render(request,'myapp/bookinghistory.html',locals())
    else:
        context["error"]="sorry no ticked booked in this account"
        return render(request,'myapp/findbus.html', context)

@login_required(login_url='signin')
def cancel(request):
    if request.method=='POST':
        id_r=request.POST.get('bus_id')

        try:
            book=Book.objects.get(id=id_r)
            bus=Bus.objects.get(id=book.busid)
            rem_r=bus.rem+book.nos
            Bus.objects.filter(id=book.busid).update(rem=rem_r)

            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect(bookinghistory)
        except Book.DoesNotExist:
            context["error"]="sorry, notticked booked tocancel"
            return render(request,'myapp/findbus.html',context)

    else:
        return render(request, 'myapp/findbus.html')


def signup(request):
    context={}
    if request.method=='POST':
        email_r=request.POST.get('email')
        name_r=request.POST.get('name')
        password_r=request.POST.get('password')
        user=User.objects.create_user(email_r,name_r,password_r)
        if user:
            login(request,user)
            return render(request,'myapp/thank.html')
        else:
            context["error"]="Invalid credintial"
            return render(request, 'myapp/signup.html',context)
    else:

        return render(request, 'myapp/signup.html')

def signin(request):
    context={}
    if request.method=='POST':
        name_r=request.POST.get('name')
        password_r=request.POST.get('password')
        user=authenticate(request,username=name_r, password=password_r)
        if user:
            login(request, user)
            context["user"]=name_r
            context["id"]=request.user.id
            return render(request,'myapp/success.html',context)
        else:
            context["error"]="Invalid credintial"
            return render(request,'myapp/signin.html', context)
    else:
        return render(request, 'myapp/signin.html',context)

def signout(request):
    context={}
    logout(request)
    context["error"]="Loggedout successfully"
    return  render(request,'myapp/signin.html', context)



def success(request):
    context={}
    context['user']=request.user
    return render(request,'myapp/success.html',context)