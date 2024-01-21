import random
import os
import time
import requests
import json
from core.engine import *
from core.intents import *
# from core.manage_intents import *

# Load Secret Keys
from dotenv import load_dotenv
load_dotenv()

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Matched Intent Response
def response(matched_intent,
             city=None,
             description=None,
             temperature=None):

    # Functional Intent Response
    if matched_intent == 'weather':
        weather_responses = [response['responses']
                             for response in intents if response['tag'] == 'weather']
        if weather_responses:
            response = random.choice(weather_responses[0])
            print(GREEN + response.format(city=city,
                                          description=description,
                                          temperature=temperature) + RESET)
        else:
            print(RED + "Error: Unable to find weather data. Check your internet connection." + RESET)

    # Default response
    else:
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


""" Weather Forecast """


def weather_forecast():
    responses = [
        f"Sure! What city would you like the weather forecast for?",
        f"I'd be happy to check the weather. Could you please tell me the city?",
        f"Great! To provide the weather forecast, I just need to know the city name. What city are you interested in?"
    ]

    print(GREEN +  random.choice(responses) + RESET)

    city = speech_recognize(recognizer, stream)

    # If the recognized city is blank, set default to "Kathmandu"
    city = city if city.strip() else "Kathmandu"

    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"{base_url}q={city}&appid={api_key}"
    response = requests.get(url)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        return f"Error: Could not retrieve weather data for {city}. Please try again later."

    if response.status_code == 200:
        # Save JSON response to a file
        file_path = 'data_archive/weather_data.json'
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(response.json(), json_file, ensure_ascii=False, indent=4)

        # Load JSON file
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        description = data.get("weather", [{}])[0].get("description")

        # Extracting temperature (Kelvin to Celsius)
        temperature = data.get("main", {}).get("temp")
        if temperature is not None:
            temperature -= 273.15
            temperature = round(temperature, 2)
        else:
            temperature = "N/A"

        return city, description, temperature
    else:
        print(
            f"Error: {response.status_code}. Could not retrieve weather data for {city}.")
        return f"Error: Could not retrieve weather data for {city}. Please try again later."



if __name__ == "__main__":
    # Intent Path
    intents = load_intents('intents.json')

    # Initialize model
    recognizer, mic, stream = initialize_model()
    print("Model Loaded Successfully...\n")
    print(GREEN + "Hello! Ask me anything or say 'goodbye' to exit." + RESET)

    while True:
        try:
            user_input = speech_recognize(recognizer, stream)
            print(user_input)

            matched_intent = None
            for item in intents:
                if match_intent(user_input, item):
                    matched_intent = item['tag']
                    break

            if matched_intent == 'Create':
                response(matched_intent)
                create_folder()

            elif matched_intent == 'Delete':
                response(matched_intent)
                delete_folder()

            elif matched_intent == 'weather':
                try:
                    city, description, temperature = weather_forecast()
                    # If the speech_recognizer is not able to parse city name re-run the recognizer instance
                    while not city:
                        print("I'm sorry, I couldn't understand the city name. Could you please rephrase it?")
                        city = speech_recognize(recognizer, stream)
                        if not city:
                            print("I still couldn't understand the city name. Please try again.")

                    response(matched_intent, city, description, temperature)
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Weather data retrieval failed.")
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    print("An unexpected error occurred during weather data retrieval.")
                    time.sleep(1)  # Sshort sleep to handle errors and prevent continuous looping
                    break  # Stop the loop if an exception occurs
            
            else:
                response(matched_intent)

            # Terminate session
            for intent in intents:
                if intent['tag'] == 'goodbye' and match_intent(user_input, intent):
                    exit()

        except Exception as e:
            print(f"Error in speech recognition: {e}")
            time.sleep(1)