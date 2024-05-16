from django.db import models


class RestaurantData(models.Model):
    restaurant_name = models.CharField(max_length=100)
    date = models.DateField()
    planned_hours = models.IntegerField()
    actual_hours = models.IntegerField()
    hours_difference = models.IntegerField()
    budget = models.FloatField()
    sells = models.FloatField()
    money_difference = models.FloatField()

    def __repr__(self):
        return f"{self.restaurant_name} - {self.date}"
