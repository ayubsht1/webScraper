# scraper/views.py
from django.http import HttpResponse
from .scraper import scrape_website
from .models import Headline
from django.shortcuts import render

def scrape_view(request):
    scrape_website()
    return HttpResponse("Scraping Complete")

def display_headlines(request):
    headlines = Headline.objects.all()  # Get all scraped headlines from the database
    return render(request, 'headlines.html', {'headlines': headlines})