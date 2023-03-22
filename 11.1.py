import requests

# hae satunnainen Chuck Norris -vitsi
response = requests.get("https://api.chucknorris.io/jokes/random")

# tarkista, että pyyntö onnistui
if response.status_code == 200:
    # tulosta vitsin teksti
    data = response.json()
    print(data["value"])
else:
    print("Vitsin hakeminen epäonnistui.")
