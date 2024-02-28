"""
Project Name: Simple Voice Assistant
Project Objective: To create a command-line voice that responds to basic queries and tells current date and system time
Project Key Features: Greetings, Replying to name inquiry and responding appropriately of a query is not
understood


NB - We will need two libraries, one which can recognise speech and another which converts a text into speech
even when offline and a date time module to get the current date and time
"""


# Library for performing speech recognition, with support for several engines and APIs, online and offline.
# It uses Google Speech Recognition  Service
import speech_recognition as sr

# pyttsx3 is a text-to-speech conversion library in Python.
# Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
import pyttsx3

import datetime

# Initialize the recognizer
# and obtains audion using system's microphone
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to get the current date
def get_date():
    return datetime.datetime.now().strftime("%A, %B %d, %Y")

# Function to get the current time
def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

# Function to speak the given text
# It outputs the given text in the code assigned for the voice assistant
# as a sound using the computer's speakers by utilizing the pyttsx module
def speak(text):
    engine.say(text)      # instructs the text-to-speech engine (engine) to speak the provided text.
    engine.runAndWait()   # ensures that the text-to-speech engine processes and speaks the text immediately.
    # Without this line, the text might not be spoken until the program reaches a point where it can wait for the
    # speech to finish

# Function to listen for user input, it listens for user input using the microphone and then attempts to recognize the
# speech using the Google Speech Recognition service.
def listen():

    # initializes a microphone object and assigns it to the variable source. The with statement ensures that the
    # microphone resource is properly released after its use.
    with sr.Microphone() as source:
        # prints a message to indicate that the program is listening for user input.
        print("Listening...")
        # adjusts the recognizer for ambient noise to improve the accuracy of speech recognition.
        recognizer.adjust_for_ambient_noise(source)
        #  captures audio input from the microphone and stores it in the audio variable.
        audio = recognizer.listen(source)

    # a try-except block to handle potential errors during speech recognition.
    try:
        # prints a message to indicate that the program is attempting to recognize the speech.
        print("Recognizing...")
        # uses the Google Speech Recognition service to recognize the speech from the captured audio and assigns the
        # recognized text to the query variable.
        query = recognizer.recognize_google(audio)
        #  prints the recognized text to the console
        print(f"User said: {query}")
        return query

    # catches an UnknownValueError exception, which occurs when the speech recognizer is unable to understand the audio.
    # and prints a message indicating that the program could not understand the user's speech.
    # and returns an empty string as the output of the listen() function in case of an error.
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return ""

    # catches a RequestError exception, which occurs when there is an issue with the Google Speech Recognition service.
    # and prints an error message indicating the specific issue with the Google Speech Recognition service.
    # and returns an empty string as the output of the listen() function in case of a request error.
    except sr.RequestError as e:
        print(f"Request error from Google Speech Recognition service; {e}")
        return ""

# Main function to handle user queries
def main():
    # This line uses the speak() function to greet the user and prompt them for their input.
    speak("Hello! How can I assist you today?")

    # This line starts an infinite loop, allowing the program to continuously listen for user input and respond
    # accordingly.
    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there! How can I help?")
        elif "what is your name" in query:
            speak("I am your virtual assistant.")
        elif "are you real?" in query:
            speak("I only exist in the virtual world.")
        elif "tell me the date" in query:
            date = get_date()
            speak(f"Today is {date}.")
        elif "tell me the time" in query:
            time = get_time()
            speak(f"The current time is {time}.")
        # If the user wants to exit, the program responds with a farewell message and breaks out of the loop,
        # ending the program
        elif "exit" in query:
            speak("Goodbye!")
            break
        # This line serves as a catch-all for any other input that the program doesn't recognize
        else:
            speak("I'm sorry, I don't understand. Can you please repeat?")

if __name__ == "__main__":
    main()
