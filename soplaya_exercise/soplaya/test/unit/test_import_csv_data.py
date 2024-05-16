import pathlib

from django.core.management import call_command, CommandError
from django.urls import reverse
from rest_framework import status
from rest_framework.test import testcases


class TestImportCSVData(testcases.TestCase):
    def setUp(self):
        self.url = reverse('restaurants-view')

    def test_import_valid_csv_data(self):
        csv_path = str(pathlib.Path(__file__).parent.resolve()) + '/dummy_data/dummy_data.csv'
        call_command('import_dataset', csv_path)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_import_without_arguments(self):
        call_command('import_dataset')
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_import_wrong_path_file(self):
        csv_path = 'invalid'
        with self.assertRaises(CommandError) as context:
            call_command('import_dataset', csv_path)

    def test_import_low_batch_size(self):
        csv_path = str(pathlib.Path(__file__).parent.resolve()) + '/dummy_data/dummy_data.csv'
        call_command('import_dataset', csv_path, batch_size=1)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_import_wrong_data(self):
        csv_path = str(pathlib.Path(__file__).parent.resolve()) + '/dummy_data/wrong_dummy_data.csv'
        with self.assertRaises(CommandError) as context:
            call_command('import_dataset', csv_path, batch_size=1)
