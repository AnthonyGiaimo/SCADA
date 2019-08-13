"""
This is the main function for the Exodus AI system.
She will be able to look up information for the owner.
"""

import pyaudio
import googleapiclient
import monotonic
import os
import speech_recognition as sr
from Command_Library import initialize, findResponse, listen, writeNewResponse, identifyCommand


def main():
    end = False
    initialize()
    while (end != True):
        audioText = raw_input("Type Something: ")
        # audioText = listen()
        print(audioText)
        responseText, type_of_command = findResponse(audioText)
        if (responseText == "kill_process"):
            end = True
        elif (type_of_command == "command"):
            identifyCommand(responseText, audioText)
        elif (type_of_command == "social"):
            os.system('./speech.sh ' + responseText)


if __name__ == "__main__":
    main()
