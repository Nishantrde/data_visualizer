from django.urls import path
from .views import * 

urlpatterns = [
    path("api/data", DataExtractor.as_view()),
    path('visualizer/', data_visualizer, name='data_visualizer'),
    
]



