from celery import Celery 
import speech_recognition as sr

r = sr.Recognizer()

app = Celery("app",
             broker="redis://localhost:6379",
             backend="db+sqlite:///results.db")

@app.task
def speech_to_text(audio_file): 
    with sr.AudioFile(audio_file) as source:
        audio_text = r.listen(source)

        try:
            text = r.recognize_google(audio_text)
            return ("Converting audio to text...\n" + text)
        except:
            return("Sorry...please try again.")