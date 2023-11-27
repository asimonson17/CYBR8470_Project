from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from Tracker.models import Dog, Breed
from Tracker.serializers import TrackerSerializer, UserSerializer
# from django.http import Http404
# from rest_framework.views import APIView
from rest_framework import viewsets, filters, parsers, renderers
# from rest_framework.response import Response
# from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .models import Tracker, User
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.forms import Form
from .forms import RegisterForm


def index(request):
    return render(request, "index.html")

    # can pass context in with render. Look at jquery over render

def addentry(request):
    return render(request, "entry.html")

    # can pass context in with render. Look at jquery over render

def calendar(request):
    return render(request, "calendar.html")


def registeruser(response):
    form=Form()
    if response.method == "POST":
	    form = Form(response.POST)
    if form.is_valid():
	    form.save()
	    return redirect("index.html")
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

"""def UserLoggedIn(request):
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

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

