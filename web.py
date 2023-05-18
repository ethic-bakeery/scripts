import requests
from bs4 import BeautifulSoup

url = 'https://receive-smss.com/sms/18622739871/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

phone_number = soup.select_one('.number > h3').text.strip()
print(phone_number)

