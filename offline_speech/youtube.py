import pywhatkit as p
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
    print('Please speak the query...')
    query = listen()

    # The following line assumes that you want to play the recognized text on YouTube using pywhatkit.
    # Make sure the recognized text is suitable for searching on YouTube.
    p.playonyt(query)
