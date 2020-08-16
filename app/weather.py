from requests import get
from json import loads


def get_weather(city):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=pl&appid=dbd1ed1a0f660663ce55eebde9dd8ceb'
        response = get(url)
        data = loads(response.text)

        return {
            'icon': data['weather'][0]['icon'],
            'city_name': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp']
        }
    except:
        return {
            'error_msg': 'Chyba mamy problemy z API'
        }
