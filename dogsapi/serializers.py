from rest_framework import serializers
from .models import Dog, Breed


class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = ('url', 'name', 'age', 'breed', 'gender', 'color', 'favorite_food', 'favorite_toy')
                  
class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ('url', 'name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'excercise_needs')
        