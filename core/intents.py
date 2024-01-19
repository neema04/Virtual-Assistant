import json
import random

def load_intents(file_path):
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents['intents']

def get_response(intent, intents):
    for item in intents:
        if item['tag'] == intent:
            responses = item['responses']
            return random.choice(responses)
    return "I'm sorry, I don't understand that. Can you please rephrase?"

def match_intent(user_input, intent):
    for pattern in intent['patterns']:
        if pattern.lower() in user_input:
            return True
    return False