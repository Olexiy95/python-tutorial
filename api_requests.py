import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

json_response = response.json()

sample_response = {
    "icon_url" : "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id" : "Zd8oOCk2TjWnugquiYPgEA",
    "url" : "",
    "value" : "mount st. helens was never an active volcano, Chuck Norris just went a few days without masturbating"
}

print(json_response['value'])