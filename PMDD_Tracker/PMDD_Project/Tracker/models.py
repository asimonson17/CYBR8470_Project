from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Value Validatators to check integer values for input validation
# Create your models here.

class PMDD(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)
  
    def __str__(self):
        return str(self.id) + " - " + self.name  