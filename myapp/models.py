from django.db import models


# Create your models here.
# Create your models here.

class Bus(models.Model):
    bus_name=models.CharField(max_length=30)
    source=models.CharField(max_length=30)
    dest=models.CharField(max_length=30)
    nos=models.DecimalField(decimal_places=0,max_digits=2)
    rem=models.DecimalField(decimal_places=0, max_digits=2)
    price=models.DecimalField(decimal_places=2,max_digits=6)
    date=models.DateField()
    time=models.TimeField()

class User(models.Model):
    used_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
class Book(models.Model):
    BOOKED="B"
    CANCELLED="C"
    TICKET_STATUS=((BOOKED,'Booked'), (CANCELLED,'Cancelled'))
    email=models.EmailField()
    name=models.CharField(max_length=30)
    userid=models.DecimalField(decimal_places=0,max_digits=3)
    busid=models.DecimalField(decimal_places=0,max_digits=3)
    bus_name=models.CharField(max_length=30)
    source=models.CharField(max_length=30)
    dest=models.CharField(max_length=30)
    nos=models.DecimalField(decimal_places=0,max_digits=2)
    price=models.DecimalField(decimal_places=0,max_digits=6)
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(choices=TICKET_STATUS, default=BOOKED, max_length=2)



