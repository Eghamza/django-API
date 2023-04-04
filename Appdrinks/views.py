from django.shortcuts import render
from django.http import JsonResponse
from .models import drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view


def drink(request):
    drink = drinks.objects.all()
    serializer = DrinkSerializer(drink, many=True)
    return JsonResponse(serializer.data, safe=False)

# Create your views here.
