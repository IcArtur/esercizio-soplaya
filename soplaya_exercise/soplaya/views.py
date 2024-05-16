from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import RestaurantData
from .serializers import RestaurantDataSerializer


class RestaurantDataList(generics.ListAPIView):
    serializer_class = RestaurantDataSerializer

    def get_queryset(self):
        queryset = RestaurantData.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        order_by = self.request.query_params.get('order_by')
        sort_order = self.request.query_params.get('sort_order')
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        if order_by:
            if order_by.lower() not in RestaurantData.get_model_fields():
                raise ValidationError({"order_by": "Specify an available field to order_by."})
            sort_prefix = '-' if sort_order and sort_order.lower() == 'desc' else ''
            order_by = sort_prefix + order_by
            queryset = queryset.order_by(order_by)
        return queryset
