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

### API Refrences
Below is a list of websites and APIs used in this project. Click on the links to access their documentation and obtain the necessary information.

- [Open Weather Map](https://openweathermap.org/api)

*Make sure to review the documentation for each API to understand their usage and any specific requirements, such as obtaining API keys or authentication tokens.*

### Setting Up API Key
- Create a `.env` file in the main directory of the project. Inside the `.env` file, define the variable for your *API key*

```bash
WEATHER_API_KEY = "{{secret.YOUR_API_KEY}}"
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

---
Feel free to send issues if you face any problem.