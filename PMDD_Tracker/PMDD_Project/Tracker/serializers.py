from rest_framework import serializers
from Tracker.models import User, Tracker #, LANGUAGE_CHOICES, STYLE_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):    
    email = forms.EmailField()
    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ['firstname', 'lastname', 'date', 'periodflow', 'irritation', 'sadness', 'happiness', 'loneliness']

#class RegisterForm(UserCreationForm):
#    email = forms.EmailField()
#    class Meta:
#	    model = User
#	    fields = ["username", "email", "password1", "password2"]


#class PMDDSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = PMDD
#        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']