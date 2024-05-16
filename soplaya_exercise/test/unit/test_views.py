from datetime import datetime

from api.models import RestaurantData
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

DATA = [
    {'restaurant_name': 'Ristorante A', 'date': datetime(2024, 1, 1), 'planned_hours': 10, 'actual_hours': 8,
     'hours_difference': 2, 'budget': 1000.43, 'sells': 800.24, 'money_difference': 200.19},
    {'restaurant_name': 'Ristorante B', 'date': datetime(2024, 1, 2), 'planned_hours': 8, 'actual_hours': 9,
     'hours_difference': 1, 'budget': 1200.52, 'sells': 1000.12, 'money_difference': 200.40},
    {'restaurant_name': 'Ristorante C', 'date': datetime(2024, 1, 3), 'planned_hours': 9, 'actual_hours': 9,
     'hours_difference': 0, 'budget': 1500.76, 'sells': 1699.12, 'money_difference': float('-198.36')}
]


class TestViews(APITestCase):
    def setUp(self):
        self.url = reverse('restaurants-view')
        restaurant_data_list = [RestaurantData(**data_dict) for data_dict in DATA]
        RestaurantData.objects.bulk_create(restaurant_data_list)

    def test_filter_date_range(self):
        response = self.client.get(self.url, {'start_date': '2024-01-01', 'end_date': '2024-01-02'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        for restaurant_data in response.data:
            response_date = datetime.strptime(restaurant_data['date'], '%Y-%m-%d')
            self.assertTrue(datetime(2024, 1, 1) <= response_date <= datetime(2024, 1, 2))

    def test_filter_date_start(self):
        response = self.client.get(self.url, {'end_date': '2024-01-01'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        for restaurant_data in response.data:
            response_date = datetime.strptime(restaurant_data['date'], '%Y-%m-%d')
            self.assertLessEqual(response_date, datetime(2024, 1, 1))


    def test_ordering(self):
        response = self.client.get(self.url, {'order_by': 'restaurant_name', 'sort_order': 'desc'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['restaurant_name'], 'Ristorante C')


    def test_ordering_restaurant_name(self):
        response = self.client.get(self.url, {'order_by': 'restaurant_name', 'sort_order': 'desc'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['restaurant_name'], 'Ristorante C')

    def test_invalid_parameters(self):
        response = self.client.get(self.url, {'order_by': 'invalid'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

