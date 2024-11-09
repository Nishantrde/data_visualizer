import os
import django
import json
from mainapp.models import DataRecord

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_visualizer.settings")  # Replace 'data_visualizer' with your project name

# Initialize Django
django.setup()

# Path to your JSON file
json_file_path = 'jsondata.json'

# Open and load the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item in data:
        obj = DataRecord.objects.create(
            end_year=item.get("end_year"),
            intensity=item["intensity"],
            sector=item.get("sector"),
            topic=item["topic"],
            insight=item["insight"],
            url=item["url"],
            region=item.get("region"),
            start_year=item.get("start_year"),
            impact=item.get("impact"),
            added=item["added"],
            published=item["published"],
            country=item.get("country"),
            relevance=item["relevance"],
            pestle=item["pestle"],
            source=item["source"],
            title=item["title"],
            likelihood=item["likelihood"],
        )
        obj.save()
