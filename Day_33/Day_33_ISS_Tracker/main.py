import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(f"response:\n{response}")     # <Response [200]>


# response status codes
# 1XX: Hold on
# 2XX: everything successful
# 3XX: you don't have permission
# 4XX: something went wrong/file doesn't exist
# 5XX: the server screwed up/is down

# print(f"response status code:\n{response.status_code}")
# # works but not ideal
# if response.status_code != 200:
#     raise Exception("Bad response")
# # Better but not best
# if response.status_code == 404:
#     raise Exception("That resources does not exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data")
# BEST
# use the request module to handle errors
response.raise_for_status()

data0 = response.json()
# print(f"data0:\n{data0}")

data1 = response.json()["iss_position"]
# print(f"\ndata1:\n{data1}")

longitude = response.json()["iss_position"]["longitude"]
# print(f"\nlongitude:\n{longitude}")

latitude = response.json()["iss_position"]["latitude"]
# print(f"\nlatitude:\n{latitude}")

iss_position = (longitude, latitude)
print(f"iss_position: {iss_position}")