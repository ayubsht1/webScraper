import requests
from bs4 import BeautifulSoup
from .models import Headline

def scrape_website():
    # Step 1: Set the URL of the website you want to scrape
    url = 'https://www.bbc.com/news'  # You can change this to any website you want

    # Step 2: Send a GET request to fetch the raw HTML content
    response = requests.get(url)

    # Step 3: Check if the request was successful
    if response.status_code == 200:
        # Step 4: Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Step 5: Find the elements you want to scrape
        # For BBC, headlines are inside <h3> tags, but you can modify this based on the website
        headlines = soup.find_all('h2')  # This will get all <h3> elements, which are headlines

        # Step 6: Print out the headlines
        # print(f"Found {len(headlines)} headlines:\n")
        # for idx, headline in enumerate(headlines, start=1):
        #     # Get the text content of each headline and strip extra spaces
        #     headline_text = headline.get_text(strip=True)
        #     print(f"{idx}. {headline_text}")

        for headline in headlines:
            headline_text = headline.get_text(strip=True)
            if headline_text:
                # Save to the database
                Headline.objects.create(title=headline_text)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
