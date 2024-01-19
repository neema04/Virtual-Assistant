import random 

from core.engine import initialize_model, speech_recognize
from core.intents import load_intents, get_response, match_intent

# from core.functions.manage_folders import create_folder, delete_folder


""" Speech Recognition for transcript """
# Transcript
# transcript = ''

# if __name__ == "__main__":
#     # call instance of Speech Engine
#     recognizer, mic, stream = initialize_model()

#     while True:
#         data=stream.read(4096)
#         if recognizer.AcceptWaveform(data):
#             result = recognizer.Result()[14:-3]
#             transcript += result + ' '
#             print(transcript)

# ANSI escape codes for colors
GREEN = "\033[92m"
RESET = "\033[0m"

if __name__ == "__main__":
    print("Chatbot: Hello! Ask me anything or say 'goodbye' to exit.")
    intents = load_intents('intents.json')

    recognizer, mic, stream = initialize_model()
    print("Model Loaded Successfully...")

    while True:

        user_input = speech_recognize(recognizer, stream)
        print(user_input)
        
        # Terminate session
        for intent in intents:
            if intent['tag'] == 'goodbye' and match_intent(user_input, intent):
                print("Chatbot:", GREEN + random.choice(intent['responses']) + RESET)
                exit()

        matched_intent = None
        for item in intents:
            if match_intent(user_input, item):
                matched_intent = item['tag']
                break
        
        # Response
        response = get_response(matched_intent, intents)
        print(GREEN + response + RESET)