from account.models import Region, District
import json
from pathlib import Path
from django.http import HttpResponse

BASE_DIR = Path(__file__).parent
path = BASE_DIR / 'regions.json'


def areas():
    if not Region.objects.all().exists():
        with open(path, 'r', encoding="utf8") as file:
            regions_data = json.load(file)

        regions = regions_data.get('regions')
        districts = regions_data.get('districts')

        region_objects = [Region(**item) for item in regions]
        district_objects = [District(**item) for item in districts]

        Region.objects.bulk_create(region_objects)
        District.objects.bulk_create(district_objects)

        return 'Add successful'
    return 'Datas exists'
