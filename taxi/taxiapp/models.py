from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{3,12}$',
)

class Car(models.Model):
    number = models.CharField(max_length=50, default=123)
    car_brand = models.CharField(max_length=50, default='Toyta')
    is_free = models.BooleanField(default=True)


class Order(models.Model):
    name = models.CharField(max_length=50,default='Михаил')
    surname = models.CharField(max_length=50,default='Яценко')
    phone_number = models.CharField(validators=[phone_regex], max_length=12,default='+380957250222')
    adress_from = models.CharField(max_length=50)
    adress_to = models.CharField(max_length=50)
    time = models.TimeField(default=timezone.now)





