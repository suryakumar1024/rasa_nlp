## happy path
* greet
  - utter_ask_search_keyword

## success path
* greet
    - utter_greet
* news_search
    - action_news_search
    - form{"name":"action_news_search"}
    - form{"name":null}
* thankyou
    - utter_goodbye

## New Story

* greet
    - utter_ask_search_keyword
* news_search{"search_keyword":"covid19"}
    - slot{"search_keyword":"covid19"}
    - action_news_search

## New Story

* greet
    - utter_ask_search_keyword
* news_search{"specific_keyword":"covid"}
    - slot{"specific_keyword":"covid"}
    - slot{"specific_keyword":"covid"}
    - utter_ask_specific_keyword_entry
* news_search{"specific_keyword":"india"}
    - slot{"specific_keyword":"india"}
    - action_news_search
    - form{"name":"action_news_search"}
    - slot{"specific_keyword":"india"}
    - slot{"specific_keyword":"india"}
    - slot{"requested_slot":"search_keyword"}

## New Story

* greet
    - utter_greet
* search_keyword_entry{"search_keyword":"current"}
    - slot{"search_keyword":"current"}
    - slot{"search_keyword":"current"}
    - utter_ask_specific_keyword_entry
* greet{"specific_keyword":"modi"}
    - slot{"specific_keyword":"modi"}
    - action_news_search
    - form{"name":"action_news_search"}
    - slot{"search_keyword":"current"}
    - slot{"specific_keyword":"modi"}
    - slot{"specific_keyword":"modi"}
    - form{"name":null}
    - slot{"requested_slot":null}

## New Story

* greet
    - utter_greet
* search_keyword_entry
    - action_news_search
    - form{"name":"action_news_search"}
    - slot{"requested_slot":"search_keyword"}
* search_keyword_entry{"specific_keyword":"india"}
    - slot{"specific_keyword":"india"}
    - slot{"specific_keyword":"india"}
    - utter_ask_specific_keyword_entry
* greet{"specific_keyword":"modi"}
    - slot{"specific_keyword":"modi"}
    - slot{"specific_keyword":"modi"}
    - action_news_search
    - slot{"specific_keyword":"modi"}
    - slot{"requested_slot":"search_keyword"}
* search_keyword_entry{"specific_keyword":"india"}
    - slot{"specific_keyword":"india"}
    - slot{"specific_keyword":"india"}
    - action_news_search
    - slot{"specific_keyword":"india"}
    - slot{"requested_slot":"search_keyword"}
    - slot{"specific_keyword":"india"}
    - slot{"specific_keyword":"modi"}
    - slot{"specific_keyword":"india"}
* search_keyword_entry{"search_keyword":"covid19"}
    - slot{"search_keyword":"covid19"}
    - action_news_search
    - slot{"search_keyword":"covid19"}
    - form{"name":null}
    - slot{"requested_slot":null}

## New Story

* greet
    - utter_ask_search_keyword
* news_search{"specific_keyword":"donald trump"}
    - slot{"specific_keyword":"donald trump"}
    - utter_ask_specific_keyword_entry
* search_keyword_entry{"search_keyword":"covid19"}
    - slot{"search_keyword":"covid19"}
    - action_news_search
    - form{"name":"action_news_search"}
    - slot{"search_keyword":"covid19"}
    - slot{"specific_keyword":"donald trump"}
    - slot{"search_keyword":"covid19"}
    - form{"name":null}
    - slot{"requested_slot":null}
