### This is a first web scraping draft ###

from bs4 import BeautifulSoup
import requests
from datetime import date

today = date.today()
url = "https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(id="cmpbox2")

print("Heutiges Datum (Jahr-Monat-Tag):", today)
print("Neuinfektionen Corona heute in Deutschland:", result)