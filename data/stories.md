## Order path
* greet
    - utter_greet
* pizza_ordering
    - pizza_form
    - form{"name":"pizza_form"}
    - form{"name":null}
* thankyou
    - utter_goodbye

## New Order Story

* greet
    - utter_greet
* toppings_entry{"food_feature":"pizza","toppings":"capsicum"}
    - slot{"food_feature":"pizza"}
    - slot{"toppings":["extra cheese","capsicum"]}
    - pizza_form
    - form{"name":"pizza_form"}
    - slot{"food_feature":"pizza"}
    - slot{"toppings":["extra cheese","capsicum"]}
    - slot{"food_feature":"pizza"}
    - slot{"toppings":["extra cheese","capsicum"]}
    - slot{"requested_slot":"pizza_type"}
* pizza_type_entry{"pizza_type":"pizza_type"}
    - slot{"pizza_type":"pizza_type"}
    - pizza_form
    - slot{"pizza_type":"pizza_type"}
    - form{"name":null}
    - slot{"requested_slot":null}

## Single intent Story

* toppings_entry{"pizza_type":"thin","food_feature":"pizza","toppings":"capsicum"}
    - slot{"food_feature":"pizza"}
    - slot{"pizza_type":"thin"}
    - slot{"toppings":["capsicum"]}
    - pizza_form
    - form{"name":"pizza_form"}
    - slot{"food_feature":"pizza"}
    - slot{"pizza_type":"thin"}
    - slot{"toppings":["capsicum"]}
    - slot{"food_feature":"pizza"}
    - slot{"pizza_type":"thin"}
    - slot{"toppings":"capsicum"}
    - form{"name":null}
    - slot{"requested_slot":null}
