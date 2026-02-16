import requests

# data = requests.get("https://dummyjson.com/products")

# result = data.json()

# for i in result.get("products"):
#     print(i.get("title"),i.get("price"))
name = input("Enter the city name: ")

data = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={name}&count=1&language=en&format=json").json()

# print(data.get('langitude'),data.get('longitude'))
for i in data.get('results'):
    print(i['latitude'],i['longitude'])
