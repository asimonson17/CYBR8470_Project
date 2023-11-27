from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.core.exceptions import ValidationError
# Value Validatators to check integer values for input validation
# Create your models here.

class PMDD(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)

  
    def __str__(self):
        return str(self.id) + " - " + self.name  

class User(models.Model):
    username = models.CharField(max_length=30, null=True, blank=False)
    email = models.CharField(max_length=30, null=True, blank=False)
    password1 = models.CharField(max_length=30, null=True, blank=False)
    password2 = models.CharField(max_length=30, null=True, blank=False)
  
    def __str__(self):
        return str(self.id) + " - " + self.name  

class Tracker(models.Model):
    firstname = models.CharField(max_length=30, null=True, blank=False)
    lastname = models.CharField(max_length=30, null=True, blank=False)
    date = models.DateField(default=datetime.date.today())
#    (validators=[
#           MinValueValidator(0),
#            MaxValueValidator(1000000)], null=True, blank=False)
    periodflow = models.CharField(max_length=30, null=True, blank=False)
    irritation = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(10)])
    sadness = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(10)])
    happiness = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(10)])
    loneliness = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(10)])

      
    def __str__(self):
        return str(self.id) + " - " + self.name  