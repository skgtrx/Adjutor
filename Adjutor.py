'''
Project : Adjutor
Description : Kivy GUI based utility application.
Author : skgtrx
Copyright : MITopen@skgtrx
'''

# Import kivy packages
from kivy.uix.textinput import TextInput
import kivy,json
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
import logging
logging.getLogger("kivy").disabled = True
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
# Import GUI Packages

# Import Modules
from module import weather
from module import wikipedia
from module import news
from module import coding
# Import Modules

# Output frame size
Window.size = (800, 600)

# Location Database 
with open('data/city.json', 'r',encoding="utf8") as f:
    data = json.load(f)
city = []
code = {}
for i in data:
    city.append(i['name'])
    code[i['name']]=i['country']
# Location Database

# Application Screens
class StartScreen(Screen):
    pass

class SelectScreen(Screen):
    pass

class WeatherScreen(Screen):
    word_list = city
    Code = code
    def suggestor(self,value):
        self.ids.city.suggestion_text = ''
        word_list = list(set(self.word_list + value[:value.rfind(' ')].split(' ')))
        val = value[value.rfind(' ') + 1:]
        if not val:
            return
        try:
            word = [word for word in word_list if word.startswith(val)][0][len(val):]
            if not word:
                return
            self.ids.city.suggestion_text = word
        except IndexError:
            pass
            #self.ids.city.insert_text(self.ids.city.suggestion_text)

    def get_weather(self):
        loc = self.ids.city.text
        loc = loc.strip()
        self.loc = loc+","+self.Code[loc]
        self.ids.loc.text = self.loc
        self.ids.weather_pic.source = 'img/'+weather.display_pic(self.loc)+'.png'
        self.ids.temp_max.text = weather.temp_max(self.loc)
        self.ids.temp_min.text = weather.temp_min(self.loc)
        self.ids.status.text = weather.status(self.loc)
        self.ids.wind.text = weather.wind_speed(self.loc)+' m/s'
        self.ids.humidity.text = weather.humidity(self.loc)
        



class NewsScreen(Screen):
    pass

class WikiSearchScreen(Screen):

    def get_wiki(self):
        text=self.ids.wiki.text
        self.ids.wikiResult.text=wikipedia.get_summary(text)

class CodingScreen(Screen):
    pass

class EndScreen(Screen):
    pass

class AdjutorApp(App):
    def build(self):
        return Builder.load_file('gui/screen.kv')
        
if __name__ == '__main__':
    AdjutorApp().run()
    

