import requests
from pprint import pprint

Api_Key = 'db51ee46fb444aeb4668b331f848f4ad'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?id="+Api_Key+"&q="+city

data = requests.get(base_url).json()
pprint(data)