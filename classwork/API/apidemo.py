import requests

data = requests.get("https://api.restful-api.dev/objects").json()
for i in data:
    print(i['id'],i['name'])




# for i in result.get("products"):
#     print(i.get("title"),i.get("price"))
# lat = 12.96
# lng = 77.57
# url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=f7e41ce7e70845cc2b06568cfc7cfb4c&units=metric"

# data = requests.get(url).json()

# print(data.get("name"))
# print("temp : ",data['main']['temp'])
# print("pressure : ",data['main']['pressure'])
# print("Humidity : ",data['main']['humidity'])
# name = "Mumbai"

# data = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={name}&count=1&language=en&format=json").json()

# # print(data.get('langitude'),data.get('longitude'))
# for i in data.get('results'):
#     # print(i['latitude'],i['longitude'])
#     print(i)
    
