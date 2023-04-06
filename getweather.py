import requests
url= "https://api.openweathermap.org/data/2.5/weather"
myapi="YOUR API KEY"

def getWeather(city):
    params = {'q':city,'appid':myapi,'lang':'tr'}
    data =requests.get(url,params=params).json()

    if data:
        city = data['name'].capitalize()
        country= data['sys']['country']
        temp = int(data['main']['temp']-273.15)
        icon = data['weather'][0]['icon']
        condition=data['weather'][0]['description'].capitalize()
        return (city,country,temp,icon,condition)