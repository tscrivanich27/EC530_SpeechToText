# app.py Dependencies
from celery import Celery 
import speech_recognition as sr

# Initialize the recognizer class and set to variable r
r = sr.Recognizer()

# Initialize a new celery app
# Hosted on Redis server: localhost, port 6379
# SQL Database: results.db
app = Celery("app",
             broker="redis://localhost:6379",
             backend="db+sqlite:///results.db")

# Define a new task for the queue system
@app.task
# Function speech_to_text converts an audio file to text
# Parameter: name of audio file
def speech_to_text(audio_file): 
    # Open the audio file and set to variable source
    with sr.AudioFile(audio_file) as source:
        # Listen to the audio file using r.listen
        audio_text = r.listen(source)

        # Attempt to recognize the contents of the file
        try:
            # Use Google speech recognition to convert audio to text
            text = r.recognize_google(audio_text)
            # Return the generated message
            return ("Converting audio to text...\n" + text)
        # If the contents of the file cannot be converted
        except:
            # Return an error message
            return("Sorry...please try again.")