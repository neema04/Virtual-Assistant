
# from automation.speech_recognition import speech_recognize, recognizer, stream
import os
import sys

# sys.path.append(realpath(join(realpath(__file__), '..', '..')))
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, '..')))

from engine import speech_recognize


"""Creation and Deletion of Directories"""
def create_folder():
    print('What do you want to name the folder?')
    folder_name = speech_recognize(recognizer, stream)
    path = f'{folder_name}'  # Replace with your desired directory

    if os.path.exists(path):
        print(f'The folder "{folder_name}" already exists at {path}')
        print('Please choose another name.')
        create_folder()
    else:
        os.mkdir(path)
        print(f'Folder "{folder_name}" created successfully at {path}')

def delete_folder():
    print('What is the name of the folder you want to delete?')
    folder_name = speech_recognize(recognizer, stream)
    path = f'{folder_name}'  # Replace with your desired directory

    if os.path.exists(path):
        os.rmdir(path)
        print(f'Folder "{folder_name}" deleted successfully.')
    else:
        print(f'The folder "{folder_name}" does not exist.')
