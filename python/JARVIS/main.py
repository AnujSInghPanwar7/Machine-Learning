import speech_recognition as sr
import webbrowser
import musicLibrary
import requests
from gtts import gTTS
import client
import pygame
import os
import time


recognizer = sr.Recognizer()

pygame.mixer.init()
def speak(text):
    print("Jarvis speaking...")

    try:
        tts = gTTS(
            text=str(text),
            lang="en",
            slow=False
        )

        tts.save("temp.mp3")

        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

        if os.path.exists("temp.mp3"):
            os.remove("temp.mp3")

        print("Finished speaking.")

    except Exception as e:
        print("TTS Error:", e)


newsapi = "35996856644c4474a72524a767f6c97c"


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open youtube music" in c.lower():
        webbrowser.open("https://music.youtube.com/")
    elif "open gmail" in c.lower():
        webbrowser.open("https://www.gmail.com/")
    elif "open reddit" in c.lower():
        webbrowser.open("https://www.reddit.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the JSON reponse
            data = r.json()

            #Extract the articles
            articles = data.get('articles',[])

            #Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        print("Asking Gemini...")

        response = client.chat.send_message(c)

        answer = response.text

        print("Jarvis:", answer)

        speak(answer)

if __name__ == "__main__":

    speak("Initializing Jarvis.")

    while True:

        print("Listening for Jarvis...")

        try:

            with sr.Microphone() as source:

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)

            print("Heard:", word)

            if "jarvis" in word.lower():

                speak("Yes, sir.")

                with sr.Microphone() as source:

                    print("Jarvis Active...")

                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=10
                    )

                command = recognizer.recognize_google(audio)

                print("Command:", command)

                processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print("Speech recognition error:", e)

        except Exception as e:
            print("Error:", e)
