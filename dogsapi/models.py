from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Breed(models.Model):
    SIZE_CHOICES = [("Tiny", "Tiny") ,("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")]
    int_validators = [MinValueValidator(1), MaxValueValidator(5)]
    
    name = models.CharField()
    size = models.CharField(choices=SIZE_CHOICES)
    friendliness = models.IntegerField(validators=int_validators)
    trainability = models.IntegerField(validators=int_validators)
    shedding_amount = models.IntegerField(validators=int_validators)
    excercise_needs = models.IntegerField(validators=int_validators)

class Dog(models.Model):
    name = models.CharField()
    age = models.PositiveSmallIntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    gender = models.CharField()
    color = models.CharField()
    favorite_food = models.CharField()
    favorite_toy = models.CharField()

