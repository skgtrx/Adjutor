'''
Project : Adjutor
Description : Kivy GUI based utility appliq_resion.
Author : skgtrx
Copyright : MITopen@skgtrx
'''

# Import kivy packages
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
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
from kivy.config import Config
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
Config.set("graphics", "width", 800)
Config.set("graphics", "height", 600)

# Location Database 
with open('data/city.json', 'r',encoding="utf8") as f:
    data = json.load(f)
city = []
code = {}
for i in data:
    city.append(i['name'])
    code[i['name']]=i['country']
# Location Database

# Appliq_resion Screens
class StartScreen(Screen):
    pass

class SelectScreen(Screen):
    def poper(self):
        popup = Popup(title='Disclaimer',content=Label(text="Slow Internet Connection\nmay lead to take\nmore time to fetch data\nKeep Patience!!!"),size_hint_x=0.3,size_hint_y=0.3)
        popup.open()

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
        news_list = news.top_headlines()
        if(len(news_list)>0):
            self.ids.top_1.text = '[b]'+news_list[0]+'[/b]'
            self.ids.top_2.text = '[b]'+news_list[1]+'[/b]'
            self.ids.top_3.text = '[b]'+news_list[2]+'[/b]'
            self.ids.top_4.text = '[b]'+news_list[3]+'[/b]'
            self.ids.top_5.text = '[b]'+news_list[4]+'[/b]'
            self.ids.top_6.text = '[b]'+news_list[5]+'[/b]'
            self.ids.top_7.text = '[b]'+news_list[6]+'[/b]'
            self.ids.top_8.text = '[b]'+news_list[7]+'[/b]'
            self.ids.top_9.text = '[b]'+news_list[8]+'[/b]'
            self.ids.top_10.text = '[b]'+news_list[9]+'[/b]'

    def headline_opener(self,ids):
        webbrowser.open(news.top_headlines_link()[ids],new=2)


class NewsByCategory(Screen):
    
    def on_parent(self,widget,parent):
        # Headlines Loader
        news_list = news.cat_headlines()
        self.ids.cat_1.text = '[b]'+news_list[0]+'[/b]'
        self.ids.cat_2.text = '[b]'+news_list[1]+'[/b]'
        self.ids.cat_3.text = '[b]'+news_list[2]+'[/b]'
        self.ids.cat_4.text = '[b]'+news_list[3]+'[/b]'
        self.ids.cat_5.text = '[b]'+news_list[4]+'[/b]'
        self.ids.cat_6.text = '[b]'+news_list[5]+'[/b]'
        self.ids.cat_7.text = '[b]'+news_list[6]+'[/b]'
        self.ids.cat_8.text = '[b]'+news_list[7]+'[/b]'
        self.ids.cat_9.text = '[b]'+news_list[8]+'[/b]'
        self.ids.cat_10.text = '[b]'+news_list[9]+'[/b]'
        self.ids.cat_11.text = '[b]'+news_list[10]+'[/b]'
        self.ids.cat_12.text = '[b]'+news_list[11]+'[/b]'
        self.ids.cat_13.text = '[b]'+news_list[12]+'[/b]'
        self.ids.cat_14.text = '[b]'+news_list[13]+'[/b]'
        self.ids.cat_15.text = '[b]'+news_list[14]+'[/b]'
        self.ids.cat_16.text = '[b]'+news_list[15]+'[/b]'
        self.ids.cat_17.text = '[b]'+news_list[16]+'[/b]'
        self.ids.cat_18.text = '[b]'+news_list[17]+'[/b]'
        self.ids.cat_19.text = '[b]'+news_list[18]+'[/b]'
        self.ids.cat_20.text = '[b]'+news_list[19]+'[/b]'
        # Link Generator
        self.news_link_list = news.cat_headlines_link()
    

    def cat_news_loader(self,category):
        news_list = news.cat_headlines(category)
        self.ids.cat_1.text = '[b]'+news_list[0]+'[/b]'
        self.ids.cat_2.text = '[b]'+news_list[1]+'[/b]'
        self.ids.cat_3.text = '[b]'+news_list[2]+'[/b]'
        self.ids.cat_4.text = '[b]'+news_list[3]+'[/b]'
        self.ids.cat_5.text = '[b]'+news_list[4]+'[/b]'
        self.ids.cat_6.text = '[b]'+news_list[5]+'[/b]'
        self.ids.cat_7.text = '[b]'+news_list[6]+'[/b]'
        self.ids.cat_8.text = '[b]'+news_list[7]+'[/b]'
        self.ids.cat_9.text = '[b]'+news_list[8]+'[/b]'
        self.ids.cat_10.text = '[b]'+news_list[9]+'[/b]'
        self.ids.cat_11.text = '[b]'+news_list[10]+'[/b]'
        self.ids.cat_12.text = '[b]'+news_list[11]+'[/b]'
        self.ids.cat_13.text = '[b]'+news_list[12]+'[/b]'
        self.ids.cat_14.text = '[b]'+news_list[13]+'[/b]'
        self.ids.cat_15.text = '[b]'+news_list[14]+'[/b]'
        self.ids.cat_16.text = '[b]'+news_list[15]+'[/b]'
        self.ids.cat_17.text = '[b]'+news_list[16]+'[/b]'
        self.ids.cat_18.text = '[b]'+news_list[17]+'[/b]'
        self.ids.cat_19.text = '[b]'+news_list[18]+'[/b]'
        self.ids.cat_20.text = '[b]'+news_list[19]+'[/b]'
        # Link Generator
        self.news_link_list = news.cat_headlines_link(category)

    def cat_headline_opener(self,ids):
        webbrowser.open(self.news_link_list[ids],new=2)

class NewsByTopic(Screen):

    def news_on_screen_loader(self):
        self.query = self.ids.newsTopic.text
        news_list = news.get_news(self.query)
        self.ids.q_res_1.text = '[b]'+news_list[0]+'[/b]'
        self.ids.q_res_2.text = '[b]'+news_list[1]+'[/b]'
        self.ids.q_res_3.text = '[b]'+news_list[2]+'[/b]'
        self.ids.q_res_4.text = '[b]'+news_list[3]+'[/b]'
        self.ids.q_res_5.text = '[b]'+news_list[4]+'[/b]'
        self.ids.q_res_6.text = '[b]'+news_list[5]+'[/b]'
        self.ids.q_res_7.text = '[b]'+news_list[6]+'[/b]'
        self.ids.q_res_8.text = '[b]'+news_list[7]+'[/b]'
        self.ids.q_res_9.text = '[b]'+news_list[8]+'[/b]'
        self.ids.q_res_10.text = '[b]'+news_list[9]+'[/b]'
        self.ids.q_res_11.text = '[b]'+news_list[10]+'[/b]'
        self.ids.q_res_12.text = '[b]'+news_list[11]+'[/b]'
        self.ids.q_res_13.text = '[b]'+news_list[12]+'[/b]'
        self.ids.q_res_14.text = '[b]'+news_list[13]+'[/b]'
        self.ids.q_res_15.text = '[b]'+news_list[14]+'[/b]'
        self.ids.q_res_16.text = '[b]'+news_list[15]+'[/b]'
        self.ids.q_res_17.text = '[b]'+news_list[16]+'[/b]'
        self.ids.q_res_18.text = '[b]'+news_list[17]+'[/b]'
        self.ids.q_res_19.text = '[b]'+news_list[18]+'[/b]'
        self.ids.q_res_20.text = '[b]'+news_list[19]+'[/b]'
        
        self.news_link_list = news.query_headlines_link(self.query)
    
    def query_opener(self,ids):
        webbrowser.open(self.news_link_list[ids],new=2)
    
class AdjutorExclusive(Screen):
    
    def on_parent(self,widget,parent):
        news_list = news.top_headlines(country='in')
        self.ids.ae_1.text = '[b]'+news_list[0]+'[/b]'
        self.ids.ae_2.text = '[b]'+news_list[1]+'[/b]'
        self.ids.ae_3.text = '[b]'+news_list[2]+'[/b]'
        self.ids.ae_4.text = '[b]'+news_list[3]+'[/b]'
        self.ids.ae_5.text = '[b]'+news_list[4]+'[/b]'
        self.ids.ae_6.text = '[b]'+news_list[5]+'[/b]'
        self.ids.ae_7.text = '[b]'+news_list[6]+'[/b]'
        self.ids.ae_8.text = '[b]'+news_list[7]+'[/b]'
        self.ids.ae_9.text = '[b]'+news_list[8]+'[/b]'
        self.ids.ae_10.text = '[b]'+news_list[9]+'[/b]'
        
        self.news_link_list = news.top_headlines_link(country='in')
    
    def headline_opener(self,ids):
        webbrowser.open(self.news_link_list[ids],new=2)

class WikiSearchScreen(Screen):

    def get_wiki(self):
        text=self.ids.wiki.text
        self.ids.wikiResult.text=wikipedia.get_summary(text)


class CodingScreen(Screen):
    
    def on_parent(self,widget,parent):
        title_list = coding.event_title()
        start_list = coding.event_start_time()
        end_list = coding.event_end_time()
        self.url_list = coding.event_url()

        # Title
        self.ids.code_title_1.text = title_list[0]
        self.ids.code_title_2.text = title_list[1]
        self.ids.code_title_3.text = title_list[2]
        self.ids.code_title_4.text = title_list[3]
        self.ids.code_title_5.text = title_list[4]
        self.ids.code_title_6.text = title_list[5]
        self.ids.code_title_7.text = title_list[6]
        self.ids.code_title_8.text = title_list[7]
        self.ids.code_title_9.text = title_list[8]
        self.ids.code_title_10.text = title_list[9]
        self.ids.code_title_11.text = title_list[10]
        self.ids.code_title_12.text = title_list[11]
        self.ids.code_title_13.text = title_list[12]
        self.ids.code_title_14.text = title_list[13]
        self.ids.code_title_15.text = title_list[14]
        self.ids.code_title_16.text = title_list[15]
        self.ids.code_title_17.text = title_list[16]
        self.ids.code_title_18.text = title_list[17]
        self.ids.code_title_19.text = title_list[18]
        self.ids.code_title_20.text = title_list[19]
        self.ids.code_title_21.text = title_list[20]
        self.ids.code_title_22.text = title_list[21]
        self.ids.code_title_23.text = title_list[22]
        self.ids.code_title_24.text = title_list[23]
        self.ids.code_title_25.text = title_list[24]
        self.ids.code_title_26.text = title_list[25]
        self.ids.code_title_27.text = title_list[26]
        self.ids.code_title_28.text = title_list[27]
        self.ids.code_title_29.text = title_list[28]
        self.ids.code_title_30.text = title_list[29]

        # Start
        self.ids.code_start_1.text = start_list[0]
        self.ids.code_start_2.text = start_list[1]
        self.ids.code_start_3.text = start_list[2]
        self.ids.code_start_4.text = start_list[3]
        self.ids.code_start_5.text = start_list[4]
        self.ids.code_start_6.text = start_list[5]
        self.ids.code_start_7.text = start_list[6]
        self.ids.code_start_8.text = start_list[7]
        self.ids.code_start_9.text = start_list[8]
        self.ids.code_start_10.text = start_list[9]
        self.ids.code_start_11.text = start_list[10]
        self.ids.code_start_12.text = start_list[11]
        self.ids.code_start_13.text = start_list[12]
        self.ids.code_start_14.text = start_list[13]
        self.ids.code_start_15.text = start_list[14]
        self.ids.code_start_16.text = start_list[15]
        self.ids.code_start_17.text = start_list[16]
        self.ids.code_start_18.text = start_list[17]
        self.ids.code_start_19.text = start_list[18]
        self.ids.code_start_20.text = start_list[19]
        self.ids.code_start_21.text = start_list[20]
        self.ids.code_start_22.text = start_list[21]
        self.ids.code_start_23.text = start_list[22]
        self.ids.code_start_24.text = start_list[23]
        self.ids.code_start_25.text = start_list[24]
        self.ids.code_start_26.text = start_list[25]
        self.ids.code_start_27.text = start_list[26]
        self.ids.code_start_28.text = start_list[27]
        self.ids.code_start_29.text = start_list[28]
        self.ids.code_start_30.text = start_list[29]

        # End
        self.ids.code_end_1.text = end_list[0]
        self.ids.code_end_2.text = end_list[1]
        self.ids.code_end_3.text = end_list[2]
        self.ids.code_end_4.text = end_list[3]
        self.ids.code_end_5.text = end_list[4]
        self.ids.code_end_6.text = end_list[5]
        self.ids.code_end_7.text = end_list[6]
        self.ids.code_end_8.text = end_list[7]
        self.ids.code_end_9.text = end_list[8]
        self.ids.code_end_10.text = end_list[9]
        self.ids.code_end_11.text = end_list[10]
        self.ids.code_end_12.text = end_list[11]
        self.ids.code_end_13.text = end_list[12]
        self.ids.code_end_14.text = end_list[13]
        self.ids.code_end_15.text = end_list[14]
        self.ids.code_end_16.text = end_list[15]
        self.ids.code_end_17.text = end_list[16]
        self.ids.code_end_18.text = end_list[17]
        self.ids.code_end_19.text = end_list[18]
        self.ids.code_end_20.text = end_list[19]
        self.ids.code_end_21.text = end_list[20]
        self.ids.code_end_22.text = end_list[21]
        self.ids.code_end_23.text = end_list[22]
        self.ids.code_end_24.text = end_list[23]
        self.ids.code_end_25.text = end_list[24]
        self.ids.code_end_26.text = end_list[25]
        self.ids.code_end_27.text = end_list[26]
        self.ids.code_end_28.text = end_list[27]
        self.ids.code_end_29.text = end_list[28]
        self.ids.code_end_30.text = end_list[29]

    def event_opener(self,ids):
        webbrowser.open(self.url_list[ids],new=2)

class EndScreen(Screen):
    pass

class AdjutorApp(App):
    def build(self):
        return Builder.load_file('gui/screen.kv')
        
if __name__ == '__main__':
    AdjutorApp().run()
    

