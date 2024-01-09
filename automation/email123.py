import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3
listner=sr.Recognizer()

tts=pyttsx3.Engine()   #line 4 and 7 are optional since they are used only to convert text to speech and the function text_to_sp is also optional

def text_to_sp(text):
    tts.say(text)
    tts.runAndWait()

def mic():
    with sr.Microphone() as source:
        print('program is listening')
        voice=listner.listen(source)
        data=listner.recognize_google(voice)
        print(data)
        return data.lower()

dict={
'saugat':'a@gmail.com',
'neema':'d@gmail.com',
'sachin':'b@gmail.com',
'sabal':'c@gmail.com'
}

def send_mail(reciever,subject,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('sendersmail@gmail.com','ap pasword key')    # syntax is server.login('senders mail','app password') for further details, see requirement.txt
    email=EmailMessage()
    email['from']="reciever_mail@gmail.com"
    email['to']=reciever
    email['subject']=subject
    email.set_content(message)
    server.send_message(email)

def main_function_code():
    text_to_sp("whom to send?")
    name = mic()

    if name in dict:
        receiver = dict[name]
        text_to_sp("what is the subject?")
        subject = mic()
        text_to_sp("what is the message?")
        message = mic()
        send_mail(receiver, subject, message)
        print("email is sent")
    else:
        print("Name not found in the dictionary.")















# def main_function_code():
#     text_to_sp("whom to send?")
#     name=mic()
#     reciever=dict[name]
#     text_to_sp("what is the subject?")
#     subject=mic()
#     text_to_sp("what is the message?")
#     message=mic()
#     send_mail(reciever,subject,message)
#     print("email is sent")



main_function_code()    