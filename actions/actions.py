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

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Interesting choice! Real-world settings can provide a grounded feel, while fantastical settings offer a sense of wonder. Do you have a preference for one over the other?"
        # Send the response back to the user
        dispatcher.utter_message(response)
        return []

class ActionCharacterPreference(Action):
    def name(self) -> Text:
        return "character_preference"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="Got it! Both settings have their charms. Now, how about characters? Do you like reading about strong, heroic figures, or do you find yourself drawn to more relatable, everyday characters?"
        # Implement logic for exploring character preferences
        return []

class ActionRelatableCharactersExplanation(Action):
    def name(self) -> Text:
        return "relatable_characters_explanation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="No worries! Let me help you figure that out. Do you have any specific traits in characters that you find interesting, like bravery, humor, or complexity?"

        # Implement logic for exploring character preferences
        return []


class ActionSpecificTopicsInterest(Action):
    def name(self) -> Text:
        return "specific_topics_interest"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="No problem! If you ever have specific questions or if there's anything you'd like to know more about, feel free to ask. Let's continue exploring your preferences!"

        # Implement logic for exploring character preferences
        return []

class ActionSportsAndOutdoorsInterest(Action):
    def name(self) -> Text:
        return "sports_and_outdoors_interest"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="That's a good starting point! Sports and outdoor activities can make for exciting and dynamic settings. Do you have a preference for a particular sport or outdoor activity in books?"
        # Implement logic for exploring character preferences
        return []


class ActionActionVsEmotionPreference(Action):
    def name(self) -> Text:
        return "action_vs_emotion_preference"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="Excellent! Balancing action and emotional moments can create a rich reading experience. Now, when it comes to length, do you prefer shorter, quick reads, or do you enjoy getting lost in longer, more immersive novels?"
        # Implement logic for exploring character preferences
        return []




class ActionBookLengthPreference(Action):
    def name(self) -> Text:
        return "book_length_preference"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="Got it!, any other informations that u want to share..?"
        # Implement logic for exploring character preferences
        return []

class ActionAskForMoreInfo(Action):
    def name(self) -> Text:
        return "ask_for_more_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="No worries! If you ever change your mind or have specific genres or themes in mind, feel free to ask for recommendations. I'm here to help whenever you're ready!, and heres your recommendation"

        # Implement logic for exploring character preferences
        return []


class ActionAcceptRecommendation(Action):
    def name(self) -> Text:
        return "accept_recommendation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="Great! Feel free to explore different genres and themes. If you ever want book recommendations or have more questions, just let me know. Happy reading!"

        # Implement logic for exploring character preferences
        return []




class ActionAskForMoreInformation(Action):
    def name(self) -> Text:
        return "action_ask_for_more_information"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="Any thing else you wanna say? "

        # Implement logic for exploring character preferences
        return []

class ActionRejectRecommendation(Action):
    def name(self) -> Text:
        return "reject_recommendation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response ="Certainly! If you have specific genres or themes in mind that you'd like to explore, or if there's anything else you'd like to discuss, feel free to let me know. I'm here to help!"

        # Implement logic for exploring character preferences
        return []


class ActionEndTheConversation(Action):
    def name(self) -> Text:
        return "action_end_the_conversation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response="Certainly! If you have specific genres or themes in mind that you'd like to explore, or if there's anything else you'd like to discuss, feel free to let me know. I'm here to help!"
        return []








