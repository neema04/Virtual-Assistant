
# from automation.speech_recognition import speech_recognize, recognizer, stream
import os
import sys

"""Creation and Deletion of Directories"""
def create_folder():
    folder_name = speech_recognize(recognizer, stream)
    path = f'{folder_name}'  # Replace with your desired directory

    if os.path.exists(path):
        print(f'The folder "{folder_name}" already exists at {path}')
        print('Please choose another name.')
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
