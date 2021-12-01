### This is a web scraping script ###

from bs4 import BeautifulSoup
import requests
from datetime import date

today = date.today()
url = "https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(id="cmpbox2")

print("Current date (Year-Month-Day):", today)
print("Daily new Covid cases in Germany:", result)