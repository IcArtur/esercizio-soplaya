from rest_framework import serializers
from .models import RestaurantData


class RestaurantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantData
        fields = '__all__'
