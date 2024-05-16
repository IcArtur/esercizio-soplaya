import csv
import os
from datetime import datetime

from api.models import RestaurantData
from backend import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


@transaction.atomic
class Command(BaseCommand):
    help = "Import restaurant data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, nargs='?')
        parser.add_argument('batch_size', type=str, nargs='?')


    def handle(self, *args, **options):
        file_path = options.get('csv_path', None)
        if not file_path:
            base_dir = settings.BASE_DIR
            file_path = os.path.join(base_dir, 'dataset.csv')
        else:
            file_path = os.path.abspath(file_path)
        batch_size = 500 if not options.get('batch_size', None) else options['batch_size']
        batch = []
        try:
            with open(file_path, 'r') as f:
                csv_rows = csv.DictReader(f)
                for row_num, row in enumerate(csv_rows):
                    try:
                        batch.append(self._create_restaurant_data(row))
                    except (ValueError, KeyError) as e:
                        raise CommandError(f"Could not parse the row {row_num + 1}. Error: {e}")
                    if len(batch) >= batch_size:
                        RestaurantData.objects.bulk_create(batch)
                        batch.clear()
                if batch:
                    RestaurantData.objects.bulk_create(batch)
        except FileNotFoundError:
            raise CommandError(
                f"I could not find the dataset file at this path: {str(file_path)}. Remember to add the file inside the"
                f" soplaya_exercise folder. ")

        self.stdout.write("Data imported successfully.")

    @staticmethod
    def _create_restaurant_data(row) -> RestaurantData:
        return RestaurantData(
            restaurant_name=row["restaurant"],
            date=datetime.strptime(row["date"], '%Y-%m-%d').date(),
            planned_hours=int(row["planned_hours"]),
            actual_hours=int(row["actual_hours"]),
            hours_difference=RestaurantData.get_hours_difference(int(row["planned_hours"]), int(row["actual_hours"])),
            budget=float(row["budget"]),
            sells=float(row["sells"]),
            money_difference=RestaurantData.get_money_difference(float(row["budget"]), float(row["sells"]))
        )
