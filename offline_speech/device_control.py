# import os
# from vosk import Model, KaldiRecognizer
# import pyaudio

# model_path = '/home/saugat/Desktop/mj1/vosk-model-small-en-in-0.4'
# model = Model(model_path)
# recognizer = KaldiRecognizer(model, 16000)
# mic = pyaudio.PyAudio()

# def listen():
#     stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    
#     print('Program is listening...')
#     audio_data = b''
    
#     while True:
#         data = stream.read(4096)
#         audio_data += data
        
#         if recognizer.AcceptWaveform(data):
#             result = recognizer.Result()[14:-3]
#             stream.stop_stream()
#             stream.close()
#             mic.terminate()
#             return result.lower()

# if __name__ == "__main__":
#     choice = listen()

#     if choice == 'shutdown' or choice == 'shutdown':
#         os.system('shutdown /s /t 20')
#         print('Shutting down in 20 seconds...')
#     elif choice == 'logoff' or choice == 'log off':
#         os.system('shutdown /l /t 20')
#         print('Logging off in 20 seconds...')
#     elif choice == 'restart' or choice == 'restart':
#         os.system('shutdown /r /t 20')
#         print('Restarting in 20 seconds...')
#     elif choice == 'nothing' or choice == 'nothing':
#         print('Okay, doing nothing.')
#     else:
#         print('Please choose one of the options: shutdown, logoff, restart, or nothing.')


#    THE ABOVE CODE IS FOR WINDOWS ONLY AND THE BELOW CODE IS FOR LINUX

import os
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

if __name__ == "__main__":
    choice = listen()

    if choice == 'shutdown' or choice == 'shutdown':
        os.system('sudo shutdown -h now')
        print('Shutting down...')
    elif choice == 'sleep' or choice == 'sleep':
        os.system('systemctl suspend')
        print('Putting the system to sleep...')
    elif choice == 'logoff' or choice == 'log off':
        os.system('gnome-session-quit --logout --no-prompt')
        print('Logging off...')
    else:
        print('Please choose one of the options: shutdown, sleep, logoff.')
