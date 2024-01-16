from core.engine import initialize_model, speech_recognize
# from core.functions.manage_folders import create_folder, delete_folder

if __name__ == "__main__":
    # call instance of Speech Engine
    recognizer, mic, stream = initialize_model()

    while True:
        data=stream.read(4096)
        if recognizer.AcceptWaveform(data):
            print(recognizer.Result()[14:-3])