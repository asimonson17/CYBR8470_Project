from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Value Validatators to check integer values for input validation
# Create your models here.

class PMDD(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)
    date = models.IntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(99)], null=True, blank=False)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    color = models.CharField(max_length=30, null=True, blank=False)
    favoritefood = models.CharField(max_length=30, null=True, blank=False)
    favoritetoy = models.CharField(max_length=30, null=True, blank=False)
    #linenos = models.BooleanField(default=False)
    #language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    #style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
      
    def __str__(self):
        return str(self.id) + " - " + self.name  