from decimal import Decimal
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import (MinValueValidator,MaxValueValidator)

from django.db import models
from .managers import UserManager
from .constants import GENDER_CHOICE

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True,null=False,blank=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def _str_(self):
        return self.email
    
@property
def balance(self):
    if hasattr(self,'account'):
        return self.account.balance
    return 0

class BankAccountType(models.Model):
    name = models.CharField(max_length=30)
    maximum_withdrawl_amount = models.DecimalField(decimal_places=2,max_digits=10)
    def _str_(self):
        self.name
class UserBankAccount(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type = models.ForeignKey(BankAccountType,related_name='accounts',on_delete=models.CASCADE)
    account_no = models.PositiveSmallIntegerField(unique=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True,blank=True)
    balance = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    initial_deposit_date = models.DateField(auto_now_add=True)
    def _str_(self):
        return self.account_no

class UserAddress(models.Model):
    user = models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    poster_code = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    def _str_(self):
        return self.user.email
    
    