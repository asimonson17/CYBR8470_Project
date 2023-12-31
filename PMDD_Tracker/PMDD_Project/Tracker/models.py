from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AnonymousUser
# Value Validatators to check integer values for input validation
# Create your models here.





class Tracker(models.Model):
    firstname = models.CharField(max_length=30, null=True, blank=False)
    lastname = models.CharField(max_length=30, null=True, blank=False)
    date = models.DateField(default=datetime.date.today())

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

        