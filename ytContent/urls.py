from django.urls import path
from .views import videoSearch

urlpatterns = [
    path('content/search',view=videoSearch)
]

