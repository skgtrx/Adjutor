from pyowm import OWM
API_key = '3100946301511a45d144316cacbf4562'
owm = OWM(API_key)
from pyowm.caches.lrucache import LRUCache
cache = LRUCache()

def temp_max(location):
    try:
        obs = owm.weather_at_place(location)
        w = obs.get_weather()
        temp = w.get_temperature(unit='celsius')['temp_max']
        return str(temp)
    except:
        return 'NA'

def temp_min(location):
    try:
        obs = owm.weather_at_place(location)
        w = obs.get_weather()
        temp = w.get_temperature(unit='celsius')['temp_min']
        return str(temp)
    except:
        return 'NA'

def status(location):
    obs = owm.weather_at_place(location)
    w = obs.get_weather()
    stat = w.get_detailed_status()
    return stat

def wind_speed(location):
    obs = owm.weather_at_place(location)
    w = obs.get_weather()
    ws = w.get_wind()['speed']
    return str(ws)

def humidity(location):
    obs = owm.weather_at_place(location)
    w = obs.get_weather()
    humidity = w.get_humidity()
    return str(humidity)

def display_pic(location):
    obs = owm.weather_at_place(location)
    w = obs.get_weather()
    pic_code = w.get_weather_icon_name()
    return pic_code
