from django.shortcuts import render
from Tracker.serializers import TrackerSerializer#, UserSerializer
# from rest_framework.views import APIView
from rest_framework import viewsets, filters, parsers, renderers
# from rest_framework.response import Response
# from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .models import Tracker#, User
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.forms import Form
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm  
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required



authentication_classes = (TokenAuthentication,)
permission_classes = (IsAuthenticated,)

def index(request):
    return render(request, "index.html")

    # can pass context in with render. Look at jquery over render

@login_required
def addentry(request):
    if request.user.is_anonymous:
        # If the user is anonymous
        return HttpResponse("You must be logged in to add an entry")
    else:
        # If the user is authenticated
        return render(request, "entry.html")

    # can pass context in with render. Look at jquery over render


@login_required
def calendar(request):
    if request.user.is_anonymous:
        # If the user is anonymous
        return HttpResponse("You must be logged in to access the calendar")
    else:
        # If the user is authenticated
        return render(request, "calendar.html")


def registeruser(response):
    form=RegisterForm()
    print(response.POST)
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            form.save()
            print("the form was valid")
            return redirect('index')
    else:
	    form = RegisterForm()
    return render(response, "registeruser.html", {"form":form})    

def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('index')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = AuthenticationForm() 
    
    return render(
        request=request,
        template_name="login.html", 
        context={'form': form}
        )

""" commeting out for tezsting
def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect(request, "index.html")
"""

class TrackerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = TrackerSerializer
    queryset = Tracker.objects.all()

    def get_queryset(self):
        currentuser = self.request.user
        print(currentuser)
        if self.request.user:
            return Tracker.objects.filter(user=currentuser.user)
        return None

""" commmenting out for testing
class UserViewSet(viewsets.ModelViewSet):
    
    A viewset for viewing and editing dog instances.
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
"""
