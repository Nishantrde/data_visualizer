from django.shortcuts import render
import json
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DataRecord
from .serializers import DataRecordSerializer
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

class DataExtractor(APIView):
    def post(self, request):
        filters = Q()  # Initialize an empty Q object to accumulate filters
        query_params = request.data

        # Iterate over each filter item to dynamically create filter criteria
        for key, value in query_params.items():
            if hasattr(DataRecord, key):
                # Check if the value is a number or date and apply an exact filter
                if isinstance(value, (int, float)) or isinstance(value, datetime):
                    filters &= Q(**{key: value})

                # Handle case-insensitive partial string matching for strings
                elif isinstance(value, str):
                    filters &= Q(**{f"{key}__icontains": value})

                # Check if the value is a dictionary (for range filtering)
                elif isinstance(value, dict):
                    if "gte" in value:
                        filters &= Q(**{f"{key}__gte": value["gte"]})
                    if "lte" in value:
                        filters &= Q(**{f"{key}__lte": value["lte"]})
            
            else:
                return Response(
                    {"error": f"Field '{key}' is not a valid field of DataRecord."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Filter DataRecord objects based on accumulated filters
        data_set = DataRecord.objects.filter(filters)

        if data_set.exists():
            serialized_data = DataRecordSerializer(data_set, many=True).data
            return Response({"data": serialized_data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No data found matching the given criteria."}, status=status.HTTP_404_NOT_FOUND)

def data_visualizer(request):
    # Convert queryset to a list of dictionaries with datetime fields formatted as strings
    data = list(DataRecord.objects.values())
    for item in data:
        item['added'] = item['added'].strftime('%Y-%m-%d %H:%M:%S') if item['added'] else None
        item['published'] = item['published'].strftime('%Y-%m-%d %H:%M:%S') if item['published'] else None
    
    # Pass JSON to template
    return render(request, 'data_visualizer.html', {"data": json.dumps(data, cls=DjangoJSONEncoder)})
