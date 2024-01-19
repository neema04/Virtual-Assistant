# Virtual Assistant

### Dependencies
To install the required Python packages you can use the following command:

```bash
pip install -r requirements.txt
```

### Run script
To run the `main.py`, load the dependencies requirements and use the following command:

```bash
py main.py
```

### Check model

```bash
from core.engine import initialize_model, speech_recognize
# Transcript
transcript = ''

if __name__ == "__main__":
    recognizer, mic, stream = initialize_model()

    while True:
        data=stream.read(4096)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()[14:-3]
            transcript += result + ' '
            print(transcript)
```