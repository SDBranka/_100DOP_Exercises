import requests
import datetime


MY_LAT = 51.507351
MY_LONG = -0.127758


# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0
# }
# response = requests.get(url="https://api.sunrise-sunset.org/json", 
#                         params=parameters
# )
# response.raise_for_status()
# data = response.json()
# print(f"data: {data}")
# sunrise = data["results"]["sunrise"]
# print(f"sunrise: {sunrise}")

# set formatted to 0 to receive time date in unix time
response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
response.raise_for_status()
data = response.json()
# print(f"data: {data}")
# access the hour value
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(f"sunrise: {sunrise}")
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(f"sunset: {sunset}")




time_now = datetime.datetime.now()
# print(f"time_now: {time_now}")
current_hour = time_now.hour
print(f"current_hour: {current_hour}")










