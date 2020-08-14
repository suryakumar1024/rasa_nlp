# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction
import requests

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


class ActionNewsSearch(FormAction):

    def name(self) -> Text:
        return "action_news_search"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["search_keyword", "specific_keyword"]

    def submit(self,
               dispatcher,
               tracker,
               domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        # import pdb;pdb.set_trace()
        search_keyword = tracker.get_slot('search_keyword')
        specific_keyword = tracker.get_slot('specific_keyword')
        result = requests.get('http://127.0.0.1:8000/querynews/',
                              params={"search_keyword": search_keyword, "specific_keyword": specific_keyword})
        df = result.json()
        # dispatcher.utter_message("receiving...")
        message = "["+df['response']['docs'][0]['abstract']+\
                  "]("+df['response']['docs'][0]['web_url']+\
                  ") \n"+df['response']['docs'][0]['lead_paragraph']
        dispatcher.utter_message(message)
        return []
