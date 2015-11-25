from gtts import gTTS
import os
import pyowm
import datetime

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

path = os.chdir('C:\\Users\Mario.carloni\Downloads')
filename = 'test.mp3'

owm = pyowm.OWM('de9716d51d0a9b8f29d668fdc5bae6ee')

city = 'New Bedford, MA'
observation = owm.weather_at_place(city)
w = observation.get_weather()
temp = w.get_temperature('fahrenheit')
status = w.get_detailed_status() 
strtemp = str(temp['temp'])

weathergreet = str('Good ' + daytime() + 
	' Mr. Carloni. The weather in ' + city + 
	' is ' + strtemp + 
	' degrees with ' + status)

tts = gTTS(text=weathergreet, lang='en')
tts.save(filename)

os.startfile('C:\\Users\\Mario.carloni\\Downloads\\' + filename)
