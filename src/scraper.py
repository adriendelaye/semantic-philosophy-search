import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://plato.stanford.edu/entries/"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "..", "data", "raw")

def scrape(topics):

    os.makedirs("data/raw", exist_ok=True)

    for topic in topics:

        url = BASE_URL + topic + "/"

        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = "\n".join(
            p.get_text().strip()
            for p in paragraphs
            if len(p.get_text()) > 50
        )
        
        file_path = os.path.join(RAW_DIR, {topics})
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
            
print("Fichier enregistré dans  {file_path} \n Scraping terminé")
