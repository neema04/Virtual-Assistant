import os
import json
import smtplib
import requests
from email.message import EmailMessage
from vosk import Model, KaldiRecognizer
import pyaudio

model_path = '/home/saugat/Desktop/mj1/vosk-model-small-en-in-0.4'
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()

def listen():
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    
    print('Program is listening...')
    audio_data = b''
    
    while True:
        data = stream.read(4096)
        audio_data += data
        
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()[14:-3]
            stream.stop_stream()
            stream.close()
            mic.terminate()
            return result.lower()

def get_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    api_key = 'your api key'
    url = f"{base_url}q={city}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        # Save JSON response to a file
        output_file_path = 'weather_data.json'
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
        
        print(f"JSON data saved to: {output_file_path}")
    else:
        print(f"Error: {response.status_code}. Could not retrieve weather data for {city}.")

if __name__ == "__main__":
    print("Please say the city name for weather information.")
    city_name = listen()

    if city_name:
        get_weather_data(city_name)
    else:
        print('No valid city name recognized.')
