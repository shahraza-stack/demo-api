import requests
import config


def get_weather(city, country_code):
    api_key = config.API_KEY['appid']
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}')
    result = response.json()
    return result


your_city = input("Enter city e.g London >")
code = input("Enter country code e.g UK >")

print(get_weather(your_city, code))
