from django.shortcuts import render
from rest_framework import generics

from .models import RestaurantData
from .serializers import RestaurantDataSerializer


class RestaurantDataList(generics.ListAPIView):
    queryset = RestaurantData.objects.all()
    serializer_class = RestaurantDataSerializer
