import requests


city = input("Anna paikkakunnan nimi: ")


api_key = "your_api_key"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)


if response.status_code == 200:

    data = response.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    print(f"Sää paikkakunnalla {city} on {description} ja lämpötila on {temperature:.1f} °C.")
else:
    print("Säätietojen hakeminen epäonnistui.")
