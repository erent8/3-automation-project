import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('h2', class_='headline')
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline.get_text()}")
    else:
        print("Web sitesine erişim başarısız oldu.")

website_url = "https://www.haberler.com"
scrape_headlines(website_url)
