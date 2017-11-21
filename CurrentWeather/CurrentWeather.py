import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
url = 'http://www.weatheronline.co.uk/weather/maps/city?LAND=LT&REGION=0004&WMO=26422&LEVEL=140'

source_code = requests.get(url, headers=headers, timeout=15)
soup = BeautifulSoup(source_code.text, "html.parser")

tables = soup.find_all('table', {'class': 'gr1'})

currentWeatherRow =  tables[0].contents[1].contents[3]
date = currentWeatherRow.contents[1].contents[0];
temperature = currentWeatherRow.contents[3].contents[0];
weather = currentWeatherRow.contents[5].contents[0];

print("Riga, current weather")
print(date, temperature + ",", weather)
