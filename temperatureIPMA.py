import requests
from datetime import datetime, timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)
afterTomorrow = tomorrow + timedelta(days=1)

today = today.strftime('%Y-%m-%d')
tomorrow = tomorrow.strftime('%Y-%m-%d')
afterTomorrow = afterTomorrow.strftime('%Y-%m-%d')

print(f"Hoje: {today}, Amanha: {tomorrow}, Depois amanha: {afterTomorrow}")

#api_url = api_url + "?api_key=" + api_key

apiTemperature = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"

response = requests.get(apiTemperature)

temperature = response.json()


for x in temperature["data"]:
    tMax = x["tMax"]
    data = x["forecastDate"]
    if data == today:
        print(f"Hoje: {tMax}")
    elif data == tomorrow:
        print(f"Amanhã: {tMax}")
    elif data == afterTomorrow:
        print(f"Depois de amanhã: {tMax}")
    else:
        print(f"{data}: {tMax}")



