
# def createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except OSError:
#         print ('Error: Creating directory. ' +  directory)
        
        


# # Example
# createFolder('/home/saugat/Desktop/data/')

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

def create_folder():
    print('What do you want to name the folder?')
    folder_name = listen()
    path = f'/home/saugat/Desktop/{folder_name}'  # Replace with your desired directory

    if os.path.exists(path):
        print(f'The folder "{folder_name}" already exists at {path}')
        print('Please choose another name.')
        create_folder()
    else:
        os.mkdir(path)
        print(f'Folder "{folder_name}" created successfully at {path}')

def delete_folder():
    print('What is the name of the folder you want to delete?')
    folder_name = listen()
    path = f'/home/saugat/Desktop/{folder_name}'  # Replace with your desired directory

    if os.path.exists(path):
        os.rmdir(path)
        print(f'Folder "{folder_name}" deleted successfully.')
    else:
        print(f'The folder "{folder_name}" does not exist.')

if __name__ == "__main__":
    print("1. Create Folder\n2. Delete Folder")
    choice = listen()

    if choice == 'create folder':
        create_folder()
    elif choice == 'delete folder':
        delete_folder()
    else:
        print('Invalid choice. Please say "create folder" or "delete folder".')
