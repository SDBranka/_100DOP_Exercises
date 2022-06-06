import requests
import os


api_key = os.environ.get("OWM_API_KEY")


# https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={api_key}
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={api_key}")
# raise an exception if the request returned an unsuccesful status code
response.raise_for_status()
# parse the JSON to obtain the quote text
weather = response.json()
print(f"weather:\n{weather}")
