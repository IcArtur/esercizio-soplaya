import typing

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

    @classmethod
    def get_model_fields(cls) -> typing.List[str]:
        return [x.name for x in cls._meta.fields]

    @staticmethod
    def get_hours_difference(planned_hours: int, actual_hours: int) -> int:
        return planned_hours - actual_hours

    @staticmethod
    def get_money_difference(budget: float, sells: float) -> float:
        return budget - sells

    def __repr__(self) -> str:
        return f"{self.restaurant_name} - {self.date}"
