## happy path 1 (/tmp/tmpbanqb46k/3c907b8c58314b978e55f29a7cb18965_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_order_placed -->


## happy path 2 (/tmp/tmpbanqb46k/3c907b8c58314b978e55f29a7cb18965_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_order_placed -->
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_order_placed -->


## sad path 1 (/tmp/tmpbanqb46k/3c907b8c58314b978e55f29a7cb18965_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_greet -->


## sad path 2 (/tmp/tmpbanqb46k/3c907b8c58314b978e55f29a7cb18965_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_ask_pizza_type -->


## sad path 3 (/tmp/tmpbanqb46k/3c907b8c58314b978e55f29a7cb18965_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_ask_pizza_type -->


## say goodbye (/tmp/tmpbanqb46k/3c907b8c58314b978e55f29a7cb18965_conversation_tests.md)
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_ask_toppings -->


## bot challenge (/tmp/tmpbanqb46k/3c907b8c58314b978e55f29a7cb18965_conversation_tests.md)
* bot_challenge: are you a bot?
    - utter_iamabot   <!-- predicted: pizza_form -->


