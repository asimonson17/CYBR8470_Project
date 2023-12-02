from django import forms
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean() 
        username_clean(self)
        email_clean(self)


    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        print("in email cleaner")
        print(new)
        print(new.count)
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  
    
