import requests

locations = ("Лондон", "SVO", "Череповец")

params = {"lang": "ru",
          "mTqn": ""
          }

for location in locations:
    url_template = "http://wttr.in/{}"
    url = url_template.format(location)
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)
