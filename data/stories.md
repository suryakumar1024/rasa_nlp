## happy path
* greet
  - utter_greet
* location_update
  - climate_form
  - form{"name":"climate_form"}
  - form{"name":null}
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story

* greet
    - utter_greet
* location_entry{"location":"chennai"}
    - slot{"location":"chennai"}
    - climate_form
    - form{"name":"climate_form"}
    - slot{"location":"chennai"}
    - slot{"location":"chennai"}
    - form{"name":null}
    - slot{"requested_slot":null}

## New Story

* greet
    - utter_greet
* location_entry{"location":"chennai"}
    - slot{"location":"chennai"}
    - climate_form
    - form{"name":"climate_form"}
    - slot{"location":"chennai"}
    - slot{"location":"chennai"}
    - form{"name":null}
    - slot{"requested_slot":null}

## New Story

* greet
    - utter_greet
* location_entry{"location":"new york"}
    - slot{"location":"new york"}
    - climate_form
    - form{"name":"climate_form"}
    - slot{"location":"new york"}
    - slot{"location":"new york"}
    - form{"name":null}
    - slot{"requested_slot":null}

## New Story

* greet
    - utter_greet
* location_entry
    - climate_form
    - form{"name":"climate_form"}
    - slot{"requested_slot":"location"}
* location_entry{"location":"china"}
    - slot{"location":"china"}
    - climate_form
    - slot{"location":"china"}
    - form{"name":null}
    - slot{"requested_slot":null}
