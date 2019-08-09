"""
This is the main function for the Exodus AI system.
She will be able to look up information for the owner.
"""

import pyaudio
import googleapiclient
import monotonic
import pyttsx3
import speech_recognition as sr
from Command_Library import initialize, findResponse, listen, writeNewResponse, identifyCommand


def main():
    end = False
    engine = initialize()
    while (end != True):
        audioText = input("Type Something: ")
        # audioText = listen()
        print(audioText)
        responseText, type_of_command = findResponse(audioText)
        if (responseText == "kill_process"):
            end = True
        elif (type_of_command == "command"):
            identifyCommand(responseText, engine, audioText)
        elif (type_of_command == "social"):
            engine.say(responseText)
            engine.runAndWait()


if __name__ == "__main__":
    main()