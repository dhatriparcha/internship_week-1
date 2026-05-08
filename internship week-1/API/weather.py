import requests

url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

response= requests.get(url)
data= response.json()

current_temp= data['current']['temperature_2m']
current_wind = data['current']['wind_speed_10m']

print(f"Temperature : {current_temp}°C")
print(f"Wind Speed  : {current_wind} km/h")
 