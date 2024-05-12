import requests



# x = requests.get(url="http://api.open-notify.org/iss-now.json")
# json_data = x.json()
# print(json_data)

SunRiseandSunSet = requests.get(url="https://api.sunrisesunset.io/json?lat=-37.7636&lng=-171.7346")

json_data = SunRiseandSunSet.json()
print(json_data)