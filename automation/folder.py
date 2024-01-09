# import os

# import smtplib
# import speech_recognition as sr
# from email.message import EmailMessage
# import pyttsx3
# listner=sr.Recognizer()

# with sr.Microphone() as source:
#         print('program is listening')
#         voice=listner.listen(source)
#         data=listner.recognize_google(voice)
#         print(data)
#         # return data.lower()

# x=data
# path='D:\{x}'
# try:
#     os.mkdir(path)
#     print('folder created')
# except FileExistsError:
#     print('folder already exists')    
# os.mkdir(path)


#this creates folder

# import os
# import speech_recognition as sr

# listener = sr.Recognizer()

# def listen():
#     with sr.Microphone() as source:
#         print('Program is listening...')
#         voice = listener.listen(source)
#         data = listener.recognize_google(voice)
#         return data.lower()

# def create_folder():
#     print('What do you want to name the folder?')
#     folder_name = listen()
#     path = f'D:\\{folder_name}'

#     if os.path.exists(path):
#         print(f'The folder "{folder_name}" already exists at {path}')
#         print('Please choose another name.')
#         create_folder()
#     else:
#         os.mkdir(path)
#         print(f'Folder "{folder_name}" created successfully at {path}')

# if __name__ == "__main__":
#     create_folder()



#this creates and deletes folder
import os
import speech_recognition as sr

listener = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print('Program is listening...')
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        return data.lower()

def create_folder():
    print('What do you want to name the folder?')
    folder_name = listen()
    path = f'D:\\{folder_name}'

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
    path = f'D:\\{folder_name}'

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
