import requests, json

with open("credentials.json","r") as data:
    creds = json.load(data)

API_KEY = creds.get("apikey")
KEYWORD = creds.get("keyword")
response = requests.get(url=f"https://newsapi.org/v2/everything?q={KEYWORD}&apiKey={API_KEY}")
response.raise_for_status()
data = response.json()

print(data)
