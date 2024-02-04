from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class UtterInitialGreetingAction(Action):
    def name(self) -> Text:
        return "utter_initial_greeting"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Hello there! I hope you're doing well. I'm here to chat with you about books. Do you have any preferences when it comes to reading?"

        # Send the response back to the user
        dispatcher.utter_message(response)

        return []


        

class UtterPreferenceSettingsAction(Action):
    def name(self) -> Text:
        return "utter_preference_settings"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic for the 'utter_preference_settings' action
        response = "Sure! Here are some preferences settings..."

        # Send the response back to the user
        dispatcher.utter_message(response)

        return []




class UtterNoPreferenceSettingsAction(Action):
    def name(self) -> Text:
        return "utter_no_preference_settings"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic for the 'utter_no_preference_settings' action
        response = "I understand. Let's explore other options."

        # Send the response back to the user
        dispatcher.utter_message(response)

        return []


class UtterUncertainCharactersAction(Action):
    def name(self) -> Text:
        return "utter_uncertain_characters"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic for the 'utter_uncertain_characters' action
        response = "It's okay not to be certain about characters. We can explore different options."

        # Send the response back to the user
        dispatcher.utter_message(response)

        return []


class UtterCertainCharactersAction(Action):
    def name(self) -> Text:
        return "utter_certain_characters"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic for the 'utter_certain_characters' action
        response = "Great! Let's talk about your preferences for certain characters."

        # Send the response back to the user
        dispatcher.utter_message(response)

        return []


class UtterContinueConversationAction(Action):
    def name(self) -> Text:
        return "utter_continue_conversation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your logic for the 'utter_continue_conversation' action
        response = "Sure! If you ever have more questions or want to discuss anything else, feel free to continue the conversation."

        # Send the response back to the user
        dispatcher.utter_message(response)

        return []