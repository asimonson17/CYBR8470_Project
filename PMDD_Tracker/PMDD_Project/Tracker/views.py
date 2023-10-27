from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets, filters, parsers, renderers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import loader

def Tracker(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
