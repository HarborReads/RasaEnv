from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionStartConversation(Action):
    def name(self) -> Text:
        return "action_start_conversation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Hello there! I hope you're doing well. I'm here to chat with you about books. Do you have any preferences when it comes to reading?"

        # Send the response back to the user
        dispatcher.utter_message(response)
        return []

class ActionExploreReadingPreferences(Action):
    def name(self) -> Text:
        return "action_explore_reading_preferences"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Awesome! It's always great to have clear preferences. Let's dive into your specific likes. Do you lean more towards fiction or non-fiction?"

        # Send the response back to the user
        dispatcher.utter_message(response)
        return []
        
class ActionRealWorldVsFantastical(Action):
    def name(self) -> Text:
        return "real_world_vs_fantastical"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_preference_settings")
        # Implement logic for exploring preferences regarding real-world vs. fantastical settings
        return []

class ActionCharacterPreference(Action):
    def name(self) -> Text:
        return "character_preference"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_no_preference_settings")
        # Implement logic for exploring character preferences
        return []

class ActionRelatableCharactersExplanation(Action):
    def name(self) -> Text:
        return "relatable_characters_explanation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_uncertain_characters")
        # Implement logic for explaining relatable characters and asking about specific traits
        return []


class ActionSpecificTopicsInterest(Action):
    def name(self) -> Text:
        return "specific_topics_interest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_no_inquire_relatable_characters")
        # Implement logic for exploring specific topics of interest
        return []

class ActionSportsAndOutdoorsInterest(Action):
    def name(self) -> Text:
        return "sports_and_outdoors_interest"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_interest_sports_outdoors")
        # Implement logic for exploring preferences related to sports and outdoors
        return []


class ActionActionVsEmotionPreference(Action):
    def name(self) -> Text:
        return "action_vs_emotion_preference"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_preference_action_emotion")
        # Implement logic for exploring preferences between action and emotion
        return []



class ActionBookLengthPreference(Action):
    def name(self) -> Text:
        return "book_length_preference"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_no_preference_action_emotion")
        # Implement logic for exploring preferences related to book length
        return []


class ActionAskForMoreInfo(Action):
    def name(self) -> Text:
        return "ask_for_more_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_no_inquire_recommendations")
        # Implement logic for asking for more information
        return []


class ActionAcceptRecommendation(Action):
    def name(self) -> Text:
        return "accept_recommendation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_accept_recommendation")
        # Implement logic for handling user acceptance of a recommendation
        return []



class ActionAskForMoreInformation(Action):
    def name(self) -> Text:
        return "action_ask_for_more_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_action_ask_for_more_information")
        # Implement logic for asking for more information
        return []

class ActionRejectRecommendation(Action):
    def name(self) -> Text:
        return "reject_recommendation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_reject_recommendation")
        # Implement logic for handling user rejection of a recommendation
        return []


class ActionEndTheConversation(Action):
    def name(self) -> Text:
        return "action_end_the_conversation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return []








