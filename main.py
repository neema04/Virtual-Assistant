import random
import os
from core.engine import initialize_model, speech_recognize
from core.intents import load_intents, get_response, match_intent
# from core.manage_folders import create_folder, delete_folder

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def response():
    response = get_response(matched_intent, intents)
    print(GREEN + response + RESET)


"""Creation and Deletion of Directories"""


def create_folder():
    folder_name = speech_recognize(recognizer, stream)
    path = os.path.abspath(folder_name)

    if os.path.exists(path):
        print(
            GREEN + f'The folder "{folder_name}" already exists at {path}' + RESET)
        print(RED + 'Please choose another name.' + RESET)
    else:
        os.mkdir(path)
        print(
            GREEN + f'Folder "{folder_name}" has been created successfully at {path}' + RESET)


def delete_folder():
    folder_name = speech_recognize(recognizer, stream)
    path = os.path.abspath(folder_name)

    if os.path.exists(path):
        os.rmdir(path)
        print(RED + f'Folder "{folder_name}" deleted successfully.' + RESET)
    else:
        print(
            RED + f'The folder named "{folder_name}" does not exist.' + RESET)


if __name__ == "__main__":
    # Intent Path
    intents = load_intents('intents.json')

    # Initialize model
    recognizer, mic, stream = initialize_model()
    print("Model Loaded Successfully...\n")
    print(GREEN + "Hello! Ask me anything or say 'goodbye' to exit." + RESET)

    while True:
        user_input = speech_recognize(recognizer, stream)
        print(user_input)

        matched_intent = None
        for item in intents:
            if match_intent(user_input, item):
                matched_intent = item['tag']
                break

        if matched_intent == 'Create':
            response()
            create_folder()

        elif matched_intent == 'Delete':
            response()
            delete_folder()

        else:
            response()

        # Terminate session
        for intent in intents:
            if intent['tag'] == 'goodbye' and match_intent(user_input, intent):
                exit()
