from rest_framework import serializers

from .models import RestaurantData


class RestaurantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantData
        fields = [
            'id',
            'restaurant_name',
            'date',
            'planned_hours',
            'actual_hours',
            'hours_difference',
            'budget',
            'sells',
            'money_difference'
        ]
