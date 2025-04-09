import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(r.text)

url = "https://lucknow.craigslist.org/"

fetchAndSaveToFile(url, "data/craigslist.html")