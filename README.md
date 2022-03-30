# EC 530 Project #4: Speech to Text Module

## Project Description 

This project is a speech to text module that will soon be included in the EC 530 Health Application. The objective is to build a queue system that will manage all speech to text operations. 

Python is the main language used for this project.

## Queue System 

The queue system is built using Celery and Redis. Celery is an asynchronous task queue. It requires the messaging queue, Redis, to send and recieve messages. Below is an image of the initialization of the Celery task queue running on a Redis server:

![#1](https://user-images.githubusercontent.com/73702777/160870082-84fdb937-13f9-4fbf-a570-59c562435ee6.JPG)

Here is an image showing how the queue system functions:

![#1](https://user-images.githubusercontent.com/73702777/160875233-dee92bce-ffbf-437e-9f89-7682a9e8ec08.JPG)

## Speech to Text

The speech to text aspect of the project is done using the Python module, PyAudio. 

The steps for audio recognition are as follows:

1) Import PyAudio library into app.py
2) Initialize audio recognizer class to variable, r 
3) For this project, all audio files have the extension .wav
4) r.listen listens to the audio file and stores in a new variable, audio_text
5) r.recognize_google(audio_text) will use Google speech recognition to convert to text

Below is an image of running the function, speech_to_text() with the parameter ("Test #1.wav")

![#2](https://user-images.githubusercontent.com/73702777/160872113-93bf2875-bbec-49ca-953f-6aa552a1bc7f.JPG)

## Database 

After converting to text, the results are sent to an SQL database titled "results.db."

The table includes all the tasks executed by Celery in a table along with the status and result.

Below is an image of the SQL table:

![#3](https://user-images.githubusercontent.com/73702777/160873074-c7f4a661-53e3-471d-9bfc-570ec2d796dd.JPG)

## Unit Tests 

1) Tests a single valid audio file -> Result: "hello how are you doing today"
2) Tests a single invalid audio file -> Result: "Sorry...please try again."
