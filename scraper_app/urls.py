# scraper/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_view, name='scrape_view'),
    path('', views.display_headlines, name='display_headlines'),  # Display scraped headlines
]
