# Data Extractor API📊

The `DataExtractor` API is designed to retrieve data from the `DataRecord` model based on dynamic filter criteria provided in the request. This API supports exact matches, partial string matches, and range filtering for numerical and date fields.

## Setup🛠

1. **Install Django and Django REST Framework**:
   ```bash
   pip install django djangorestframework

2. **Add REST Framework to Installed Apps: In your Django project’s settings, add 'rest_framework' to INSTALLED_AFPPS.**
3. **Define DataRecord Model: Make sure that the DataRecord model is defined in your models file with relevant fields (e.g., likelihood, intensity, topic, added, published, etc.).**
4. **Define Serializer: Create a serializer for DataRecord in serializers.py:**
    ```bash
    from rest_framework import serializers
    from .models import DataRecord

    class DataRecordSerializer(serializers.ModelSerializer):
        class Meta:
            model = DataRecord
            fields = '__all__'

5. **Add URL Configuration: Map the DataExtractor API view in urls.py:**
    ```bash
      from django.urls import path
      from .views import DataExtractor

      urlpatterns = [
          path('api/data/', DataExtractor.as_view(), name='data-extractor'),# api 
          path('visualizer/', data_visualizer, name='data_visualizer'),# visualizer
# Data Visualizer📈

This project is an interactive data visualization tool using HTML, CSS, and D3.js. It allows users to dynamically choose different attributes for the X and Y axes to render a bar chart based on their selections. The tool features a hover-enabled tooltip to display detailed data values and smooth transitions for a visually engaging experience.

### Key filtering features:

- **X-Axis and Y-Axis Selection**: Users can filter the chart by selecting different attributes for both axes.
- **Dynamic Chart Updates**: The chart automatically updates when new attributes are selected.
- **Tooltip**: Hover over bars to view specific data values for the selected X and Y attributes.
- **Smooth Transitions**: Visual elements like bars change dynamically with smooth transitions for a fluid user experience.

# Usage
## Endpoint
    
    POST /api/data/

## Request Body
The request body should be a JSON object containing filter criteria. Each key-value pair corresponds to a field in the DataRecord model. You can perform:

1. Exact match for numeric, date, or text fields.

2. Partial match for text fields (case-insensitive).

3. Range filtering for numeric and date fields.

# Example Requests🙏
## 1. Exact Match
**Request:**
    
    {
    "likelihood": 2,
    "topic": "oil"
    }
**Explanation:** This request retrieves all records where likelihood is exactly 2 and topic contains "oil" (case-insensitive).

## 2. Partial String Match
**Request:**

    {
      "source": "EIA"
    }
**Explanation:** This request retrieves records where the source field contains the substring "EIA".

## 3. Range Filtering🎯
**Request:**

    {
      "intensity": 6,
      "topic": "oil"
    }
**Explanation:** This request retrieves records where intensity equal to 6 and topic oil.

## Response💬

**Success (200 OK):**

    {
      "data": [
        {
          "id": 1,
          "end_year": "2025",
          "intensity": 8,
          "sector": "Energy",
          "topic": "oil",
          "added": "2022-12-31 13:45:00",
          "published": "2023-01-01 10:30:00",
          ...
        },
        ...
      ]
    }

**Error (400 Bad Request) - Invalid Field:**

    {
      "error": "Field 'invalid_field' is not a valid field of DataRecord."
    }
## Error (404 Not Found) - No Data Found:

    {
      "error": "No data found matching the given criteria."
    }

## Filtering Options

The **DataExtractor** API supports the following types of filters:

1. Exact Match: Match values exactly (for numeric, date, and string fields).

2. Partial Match: For string fields, **__icontains** is used to perform case-insensitive partial matches.

3. Range Filtering: For numeric and date fields, use **{"gte": value}** for "greater than or equal to" and **{"lte": value}** for "less than or equal to" filtering.

## Implementation Details
The **DataExtractor** API uses Django’s **Q** objects to build complex queries based on the filters specified in the request. The class dynamically identifies field types and applies the appropriate filter (exact, partial, or range) based on the data type of the request values.

1. Exact Matches: For **int**, **float**, and **datetime** values, the API applies an exact filter.

2. Partial Matches: For string values, the API uses **__icontains** to allow case-insensitive partial matching.

3. Range Filtering: If a dictionary with **gte** or **lte** keys is provided, the API applies a range filter on numeric or date fields.

# Error Handling❗⚠️
Invalid Fields: If a field does not exist in **DataRecord**, the API returns a 400 Bad Request with an error message.

No Matching Data: If no records match the criteria, the API returns a 404 Not Found response with an appropriate message.

## Examples of Advanced Usage
Retrieve records with **likelihood** greater than or equal to 3 and **published** date less than or equal to **2022-01-01:**

    {
      "likelihood": {"gte": 3},
      "published": {"lte": "2022-01-01"}
    }
Retrieve records where **sector** contains "**Energy**" and **country** contains "**USA**":

    {
      "sector": "Energy",
      "country": "USA"
    }




This README provides a detailed overview of the **DataExtractor API**, including setup instructions, request examples, filtering options, and error handling.



