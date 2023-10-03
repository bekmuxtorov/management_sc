from account.models import Region, District
import json
from pathlib import Path
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add region and district'
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    path = BASE_DIR / 'utils' / 'regions.json'
    def areas(self):
        if not Region.objects.all().exists():
            with open(self.path, 'r', encoding="utf8") as file:
                regions_data = json.load(file)

            regions = regions_data.get('regions')
            districts = regions_data.get('districts')

            region_objects = [Region(**item) for item in regions]
            district_objects = [District(**item) for item in districts]

            Region.objects.bulk_create(region_objects)
            District.objects.bulk_create(district_objects)

            return 'Region and District have been added successfully'
        return 'Datas exists'


    def handle(self, *args, **kwargs):
        self.stdout.write(self.areas())
    