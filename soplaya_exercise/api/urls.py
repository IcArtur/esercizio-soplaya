from django.urls import path
from . import views

urlpatterns = [
    path("restaurants/", views.RestaurantDataList.as_view(), name="restaurants-view"),
]