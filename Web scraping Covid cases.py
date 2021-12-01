### This is a web scraping script ###

from bs4 import BeautifulSoup
from lxml import etree
import requests
from datetime import date

today = date.today()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases';
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'lxml')

for item in soup.select('table tr'):
try:
print('----------------------------------------')

region=item.select('td')[0].get_text()
print("Region", region)
country=item.select('td')[1].get_text()
print("Land", country)
confirmed=item.select('td')[2].get_text()
print("Coronafälle", confirmed)
deaths=item.select('td')[3].get_text()
print("Todesfälle", deaths)

except Exception as e:
#raise e
print('')
print("Current date (Year-Month-Day):", today)