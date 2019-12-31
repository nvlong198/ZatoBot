from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import random
import feedparser
from gmail import get_gmail
import re
import json

class ActionSaveCusInfo(Action):

    def name(self) -> Text:
        return "action_save_cust_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        cust_name = next(tracker.get_latest_entity_values("cust_name"), None)
        cust_sex = next(tracker.get_latest_entity_values("cust_sex"), None)
        if (cust_sex is  None):
            cust_sex = "Quý khách"

        if (cust_sex == "anh") | (cust_sex == "chị"):
           bot_position = "em"
        elif (cust_sex == "cô") | (cust_sex == "chú"):
            bot_position = "cháu"
        else:
            cust_sex = "bạn"
            bot_position = "mình"
    
        return [SlotSet('cust_name', cust_name),SlotSet('cust_sex', cust_sex ),\
                SlotSet('bot_position', bot_position)]

class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        weather = requests.get('http://localhost:11223/api/weather').json()
        description = weather["response"]['description']
        temp = weather["response"]['temp']
        humidity = weather['response']['humidity']
        
        dispatcher.utter_message('`From OpenWeatherMap` :flag-vn: \nThời tiết Hà Nội\nTình trạng: {} \nNhiệt độ: {} độ C\nĐộ ẩm: {}%'.format(description, temp, humidity))
        return []

class ActionGetNews(Action):

    def name(self) -> Text:
        return "action_get_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        res = requests.get('http://localhost:11223/api/news').json()

        topic = res['topic']
        link = res['href']
        # newspaper = res['newspaper']
        time = res['update_time']
        dispatcher.utter_message('`{}`\n*Bài viết*: {}\n{}'.format(time, topic, link))

        return []

class ActionGetGmail(Action):

    def name(self) -> Text:
        return "action_get_gmail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message('\n\n'.join(get_gmail()))
        return []

class ActionGetLottery(Action):
   
   def name(self) -> Text:
            # Doan nay khai bao giong het ten ham ben tren la okie
          return 'action_get_lottery'
   
   def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            res = requests.get('http://localhost:11223/api/lottery').json()
            return_msg = '`' + res['today'] + "` :flag-vn: \n" + res['description']
            dispatcher.utter_message(return_msg)
            return []