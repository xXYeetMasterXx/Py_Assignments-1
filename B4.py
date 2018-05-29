import requests

r = requests.get("https://analytics.usa.gov/data/live/realtime.json")
print(r.json()['data'][0]['active_visitors'])
