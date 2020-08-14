# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_core_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

import requests
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionClimateWorld(FormAction):

    def name(self):  # type: () -> Text
        return "climate_form"

    @staticmethod
    def required_slots(tracker):  # type: (Tracker) -> List[Text]
        return ["location.txt"]

    def submit(self, dispatcher, tracker, domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        # import pdb;pdb.set_trace()
        location = tracker.get_slot('location.txt')
        # action_url = "http://api.openweathermap.org/data/2.5/weather?q="+location.txt+"&appid=eb1499dfb19342dd317b6b1a34a929de"
        result = requests.get("http://api.openweathermap.org/data/2.5/weather",
                              params={
                                  "q": location,
                                  "appid": "xxxxxxxxx"
                              })
        # https://www.google.com/maps/@10.8091781,78.2885026,7z
        result = result.json()
        message = "["+result["name"]+"](https://www.google.com/maps/@"+str(result["coord"]["lon"])+","+str(result["coord"]["lat"])+") Weather will be "+result['weather'][0]['main']+" "+result['weather'][0]['description']+\
                  "\n Today temprature will be"+str(result["main"]["temp"])+\
                  " but feels_like "+str(result["main"]["temp"])+" \n"+ \
                  "Expected max temperature"+str(result["main"]["temp_max"])+" and minimum is "+str(result["main"]["temp_min"])
        dispatcher.utter_message(message)
        return []
