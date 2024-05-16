from django.shortcuts import render
from rest_framework import generics

from .models import RestaurantData
from .serializers import RestaurantDataSerializer


class RestaurantDataList(generics.ListAPIView):
    serializer_class = RestaurantDataSerializer

    def get_queryset(self):
        queryset = RestaurantData.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date is not None:
            queryset = queryset.filter(date__gte=start_date)
        if end_date is not None:
            queryset = queryset.filter(date__lte=end_date)
        return queryset
