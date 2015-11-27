import datetime
import pyowm
import pyttsx

now = datetime.datetime.now()

def daytime():
    time = now.strftime("%H:%M")
    intHour = int(time[:2])
    if intHour < 12:
        return('morning')
    elif intHour > 18:
        return('evening')
    else:
        return('afternoon')

owm = pyowm.OWM('OWMAPIKEY')

city = 'CITY,STATE'
observation = owm.weather_at_place(city)
w = observation.get_weather()
temp = w.get_temperature('fahrenheit')
status = w.get_detailed_status()
strtemp = str(temp['temp'])
humid = str(w.get_humidity())
wind = w.get_wind()
getwspeed = str(wind['speed'])
getwdeg = wind['deg']

def carddir(x):
    x = int(x)
    if 0 <= x <= 89:
        return 'North'
    elif 90 <= x <= 179:
        return 'East'
    elif 180 <= x <= 269:
        return 'South'
    elif 270 <= x <= 359:
        return 'West'
    else:
        return None


weathergreet = str('Good ' + daytime() +
    ' Mr. or Mrs. Whoever. The weather in ' + city[:9] +
    ' is ' + strtemp +
    ' degrees with ' + status +
    'Windspeed ' + carddir(getwdeg) + ' at ' + getwspeed + ' miles per hour, and ' + humid + ' percent humidity.')

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)
engine.say(weathergreet)
engine.runAndWait()
