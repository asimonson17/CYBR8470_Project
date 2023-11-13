from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from Tracker.models import Dog, Breed
# from Tracker.serializers import DogSerializer, BreedSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import viewsets, filters, parsers, renderers
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "index.html")

    # can pass context in with render. Look at jquery over render
    
class TrackerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = TrackerSerializer
    queryset = Tracker.objects.all()
