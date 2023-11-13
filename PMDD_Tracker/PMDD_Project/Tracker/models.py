from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Value Validatators to check integer values for input validation
# Create your models here.

class PMDDf(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)

  
    def __str__(self):
        return str(self.id) + " - " + self.name  

class User(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)
    age = models.IntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(99)], null=True, blank=False)
    periodtype = models.CharField(max_length=30, null=True, blank=False)

      
    def __str__(self):
        return str(self.id) + " - " + self.name  

class Tracker(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)
    date = models.IntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(99)], null=True, blank=False)
    periodtype = models.CharField(max_length=30, null=True, blank=False)
    anger = models.IntegerField(validators=[
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