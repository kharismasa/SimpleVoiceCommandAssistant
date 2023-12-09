# -*- coding: utf-8 -*-
"""
@author: Kharisma
"""

import speech_recognition as sr
import pyautogui
import webbrowser
import time
import pyttsx3


video_paused = False
search_query = ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("What can I help you with, master?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I don't understand what you say. Please say it again.")
        return None
    except sr.RequestError as e:
        speak(f"Error on API request: {e}")
        return None

def scroll_up():
    pyautogui.scroll(700)
    speak("Scrolling up.")

def scroll_down():
    pyautogui.scroll(-700)
    speak("Scrolling down.")

def search_video(query):
    global search_query
    search_query = query
    #speak("Ready to search.")
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)
    webbrowser.open(f"www.youtube.com/results?search_query={query}")
    pyautogui.press("enter")
    time.sleep(2)
    speak(f"Following are the results from {query}.")

def play_video():
    pyautogui.press("k")
    speak("Video played.")

def pause_resume_video():
    global video_paused
    if not video_paused:
        pyautogui.press("k")
        speak("Video paused.")
    else:
        pyautogui.press("k")
        speak("Video resumed.")
    video_paused = not video_paused

def back():
    pyautogui.hotkey("alt", "left")
    speak("Going back to the previous page.")
    
def next():
    pyautogui.hotkey("alt", "right")
    speak("Going back to the next page.")

def save_to_watch_later():
    pyautogui.press("shift+L")
    speak("Video saved to Watch Later.")

def volume_up():
    pyautogui.press("volumeup")
    speak("Volume up.")

def volume_down():
    pyautogui.press("volumedown")
    speak("Volume down.")


def main():
    speak("Welcome, master! This is your voice assistant. You can command me to search, play, stop, scroll, go back, save video, or raise and lower the volume. To exit the program, say 'exit'. What can I help you with, master?")

    while True:
        command = listen_command()

        if command:
            if "search" in command:
                query = command.split("search")[1].strip()
                search_video(query)
            elif "play" in command:
                play_video()
            elif "stop" in command:
                pause_resume_video()
            elif "exit" in command:
                speak("Stopping the program. Goodbye, master!")
                break
            elif "back" in command:
                back()
            elif "next" in command:
                next()
            elif "scroll up" in command:
                scroll_up()
            elif "scroll down" in command:
                scroll_down()
            elif "volume up" in command:              
                volume_up()
            elif "volume down" in command:
                volume_down()
            elif "save" in command:
                save_to_watch_later()
            else:
                speak("Sorry, I don't understand what you say. Please say it again.")

if __name__ == "__main__":
    main()

