from rest_framework import serializers
from Tracker.models import User, Tracker #, LANGUAGE_CHOICES, STYLE_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator

#previously class DogSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ['firstname', 'lastname', 'date', 'periodflow', 'irritation', 'sadness', 'happiness', 'loneliness']


#class PMDDSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = PMDD
#        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']