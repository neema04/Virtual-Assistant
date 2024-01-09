
# import speech_recognition as sr
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



# device=AudioUtilities.GetSpeakers()
# interface=device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
# volume=cast(interface,POINTER(IAudioEndpointVolume))
# volume.SetMasterVolumeLevel(-12,None)

import speech_recognition as sr
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

listener = sr.Recognizer()

def get_number():
    with sr.Microphone() as source:
        print('Program is listening...')
        try:
            voice = listener.listen(source, timeout=5)
            data = listener.recognize_google(voice)
            print('You said:', data)
            # Check if the recognized input is a number
            if data.isdigit():
                return int(data)
            else:
                print("Please speak a valid number.")
        except sr.UnknownValueError:
            print("No input detected within 5 seconds. Using default or previous value.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def set_volume(x):
    device = AudioUtilities.GetSpeakers()
    interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-x, None)
    print(f"Volume adjusted to {x}.")

if __name__ == "__main__":
    # Get the number from user input
    number = get_number()

    # If no input is received, you may want to use a default or previously set value
    if number is None:
        # Use a default or previously set value
        number = 50  # Replace with your default value

    # Set the volume based on the spoken number
    set_volume(number)
