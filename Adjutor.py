'''
Project : Adjutor
Description : Kivy GUI based utility appliq_resion.
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
from kivy.properties import ObjectProperty
from kivy.core.window import Window
# Import GUI Packages

# Import Modules
from module import weather
from module import wikipedia
from module import news
from module import coding
# Import Modules

# Other Imports
import webbrowser
# Other Imports

# Output frame size
Window.size = (800, 600)

# Loq_resion Database 
with open('data/city.json', 'r',encoding="utf8") as f:
    data = json.load(f)
city = []
code = {}
for i in data:
    city.append(i['name'])
    code[i['name']]=i['country']
# Loq_resion Database

# Appliq_resion Screens
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

class TopHeadlines(Screen):

    def on_parent(self,widget,parent):
        # Headlines Loader
        self.ids.top_1.text = news.top_headlines()[0]
        self.ids.top_2.text = news.top_headlines()[1]
        self.ids.top_3.text = news.top_headlines()[2]
        self.ids.top_4.text = news.top_headlines()[3]
        self.ids.top_5.text = news.top_headlines()[4]
        self.ids.top_6.text = news.top_headlines()[5]
        self.ids.top_7.text = news.top_headlines()[6]
        self.ids.top_8.text = news.top_headlines()[7]
        self.ids.top_9.text = news.top_headlines()[8]
        self.ids.top_10.text = news.top_headlines()[9]

    def headline_opener(self,ids):
        webbrowser.open(news.top_headlines_link()[ids],new=2)


class NewsByCategory(Screen):
    
    def on_parent(self,widget,parent):
        # Headlines Loader
        news_list = news.cat_headlines()
        self.ids.cat_1.text = news_list[0]
        self.ids.cat_2.text = news_list[1]
        self.ids.cat_3.text = news_list[2]
        self.ids.cat_4.text = news_list[3]
        self.ids.cat_5.text = news_list[4]
        self.ids.cat_6.text = news_list[5]
        self.ids.cat_7.text = news_list[6]
        self.ids.cat_8.text = news_list[7]
        self.ids.cat_9.text = news_list[8]
        self.ids.cat_10.text = news_list[9]
        self.ids.cat_11.text = news_list[10]
        self.ids.cat_12.text = news_list[11]
        self.ids.cat_13.text = news_list[12]
        self.ids.cat_14.text = news_list[13]
        self.ids.cat_15.text = news_list[14]
        self.ids.cat_16.text = news_list[15]
        self.ids.cat_17.text = news_list[16]
        self.ids.cat_18.text = news_list[17]
        self.ids.cat_19.text = news_list[18]
        self.ids.cat_20.text = news_list[19]
        # Link Generator
        self.news_link_list = news.cat_headlines_link()
    

    def cat_news_loader(self,category):
        news_list = news.cat_headlines(category)
        self.ids.cat_1.text = news_list[0]
        self.ids.cat_2.text = news_list[1]
        self.ids.cat_3.text = news_list[2]
        self.ids.cat_4.text = news_list[3]
        self.ids.cat_5.text = news_list[4]
        self.ids.cat_6.text = news_list[5]
        self.ids.cat_7.text = news_list[6]
        self.ids.cat_8.text = news_list[7]
        self.ids.cat_9.text = news_list[8]
        self.ids.cat_10.text = news_list[9]
        self.ids.cat_11.text = news_list[10]
        self.ids.cat_12.text = news_list[11]
        self.ids.cat_13.text = news_list[12]
        self.ids.cat_14.text = news_list[13]
        self.ids.cat_15.text = news_list[14]
        self.ids.cat_16.text = news_list[15]
        self.ids.cat_17.text = news_list[16]
        self.ids.cat_18.text = news_list[17]
        self.ids.cat_19.text = news_list[18]
        self.ids.cat_20.text = news_list[19]
        # Link Generator
        self.news_link_list = news.cat_headlines_link(category)

    def cat_headline_opener(self,ids):
        webbrowser.open(self.news_link_list[ids],new=2)

class NewsByTopic(Screen):

    def news_on_screen_loader(self):
        self.query = self.ids.newsTopic.text
        news_list = news.get_news(self.query)
        self.ids.q_res_1.text = news_list[0]
        self.ids.q_res_2.text = news_list[1]
        self.ids.q_res_3.text = news_list[2]
        self.ids.q_res_4.text = news_list[3]
        self.ids.q_res_5.text = news_list[4]
        self.ids.q_res_6.text = news_list[5]
        self.ids.q_res_7.text = news_list[6]
        self.ids.q_res_8.text = news_list[7]
        self.ids.q_res_9.text = news_list[8]
        self.ids.q_res_10.text = news_list[9]
        self.ids.q_res_11.text = news_list[10]
        self.ids.q_res_12.text = news_list[11]
        self.ids.q_res_13.text = news_list[12]
        self.ids.q_res_14.text = news_list[13]
        self.ids.q_res_15.text = news_list[14]
        self.ids.q_res_16.text = news_list[15]
        self.ids.q_res_17.text = news_list[16]
        self.ids.q_res_18.text = news_list[17]
        self.ids.q_res_19.text = news_list[18]
        self.ids.q_res_20.text = news_list[19]
        
        self.news_link_list = news.query_headlines_link(self.query)
    
    def query_opener(self,ids):
        webbrowser.open(self.news_link_list[ids],new=2)
    
class AdjutorExclusive(Screen):
    
    def on_parent(self,widget,parent):
        # for test
        self.ids.ae_1.text = 'Headline-1'
        self.ids.ae_2.text = 'Headline-2'
        self.ids.ae_3.text = 'Headline-3'
        self.ids.ae_4.text = 'Headline-4'
        self.ids.ae_5.text = 'Headline-5'
        self.ids.ae_6.text = 'Headline-6'
        self.ids.ae_7.text = 'Headline-7'
        self.ids.ae_8.text = 'Headline-8'
        self.ids.ae_9.text = 'Headline-9'
        self.ids.ae_10.text = 'Headline-10'
    
    def headline_opener(self,ids):
        webbrowser.open(news.ae_headlines_link()[ids],new=2)

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
    

