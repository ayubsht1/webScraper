import requests
import random

proxies_list = {
    'http://52.13.248.29:1080',
}

url = 'https://lucknow.craigslist.org/'
proxy = random.choice(list(proxies_list))

try:
    response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=500)
except Exception as e:
    print(f"Proxy failed: {proxy}", e)

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(r.text)

fetchAndSaveToFile(url, "data/craigslistrequestp.html")