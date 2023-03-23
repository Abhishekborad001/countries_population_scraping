import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/world-population/population-by-country/"

response = requests.get(url)
soup = BeautifulSoup(response.text ,'html.parser')

# print(soup)

rows = soup.find('table', {'id':'example2'}).find('tbody').find_all('tr')
# print(len(rows))


countries_list = []

for row in rows:
    dic = {}
    dic['country'] = row.find_all('td')[1].text
    dic['population'] = row.find_all('td')[2].text.replace(',','')
    countries_list.append(dic)


# print(countries_list[1])

df = pd.DataFrame(countries_list)
df.to_excel('countries_population.xlsx' , index=False)
df.to_csv('countries_population.csv', index=False)