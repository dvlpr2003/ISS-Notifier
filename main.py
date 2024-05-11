import requests



x = requests.get(url="http://api.open-notify.org/iss-now.json")
json_data = x.json()
print(json_data["iss_position"]["longitude"])