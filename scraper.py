
# scraper.py

import requests

from bs4 import BeautifulSoup



url = 'http://example.com'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')



print(soup.title.text)

# Modify scraper.py

import csv



with open('data.csv', 'w', newline='') as file:

    writer = csv.writer(file)

    writer.writerow(["Title"])

    writer.writerow([soup.title.text])


additional_data = soup.find_all('p')

for data in additional_data:

    writer.writerow([data.text])

    additional_data = soup.find_all('p')

for data in additional_data:

    writer.writerow([data.text])

