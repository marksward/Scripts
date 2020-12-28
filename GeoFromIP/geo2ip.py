import settings
import requests

url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"

querystring = {"ip":"8.8.8.8"}

headers = {
    'x-rapidapi-key': settings.rapidapikey,
    'x-rapidapi-host': "ip-geolocation-ipwhois-io.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)