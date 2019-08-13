"""
This is the python file that holds all of the commands for Exodus to use.
"""

import pyttsx3
import os
import speech_recognition as sr
import command_protocols


def initialize():
    os.system('./speech.sh Hello Tony. Please wait while I get a few things ready for you')
    os.system('./speech.sh Okay, all ready. How may I help you today?')


def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            audioText = r.recognize_google(audio)
            return audioText
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    # return "open chrome"

def load_dictionary(filename):
    """
    Load a dictionary from the given file.
    Each line in the given file must contain a key/value pair separated by a colon.
    :param str filename: The file name containing a dictionary.
    :return: A dictionary with key/value pairs from the file.
    :rtype: dict[str, str]
    """
    # Start with an empty dictionary.
    d = {}
    with open(filename) as data_file:
        data_list = data_file.read().splitlines()
        for data in data_list:
            count = 0
            for count in range(len(data)):
                if data[count] == ":":
                    key = data[0:count]
                    value = data[count + 1:]
                    d[key] = (value)
                count += 1
    # Return the entire dictionary.
    return d


def findResponse(audioText):
    social_dictionary = load_dictionary("./ResponseDictionary.txt")
    command_dictionary = load_dictionary("./CommandDictionary.txt")
    if audioText == None:
        return "None", "social"
    elif (audioText[0:4] == "open"):
        return 'command_protocols.openProgram(' + '"' + audioText[5:] + '"' + ')', "command"
    elif (audioText[0:6] == "launch"):
        return 'command_protocols.openProgram(' + '"' + audioText[7:] + '"' + ')', "command"
    elif (audioText[0:3] == "run"):
        return 'command_protocols.openProgram(' + '"' + audioText[4:] + '"' + ')', "command"
    for key in social_dictionary.keys():
        if audioText.lower() == key.lower():
            return social_dictionary[key], "social"
    for key in command_dictionary.keys():
        if audioText.lower() == key.lower():
            return command_dictionary[key], "command"
    return "No found responses", "command"


def writeNewResponse(audioText):
    dictionary = load_dictionary("./ResponseDictionary.txt")
    os.system('./speech.sh What would you like my response to be for ')
    os.system('./speech.sh ' + audioText)
    newResponse = raw_input("What would you like me to say (social): ")
    # newResponse = listen()
    dictionary[audioText] = newResponse
    with open("./ResponseDictionary.txt", "a") as write_file:
        for keys in dictionary.keys():
            print(keys + ":" + dictionary[keys])
            write_file.write(keys + ":" + dictionary[keys])
    os.system('./speech.sh Okay, done!')


def writeNewCommand(audioText):
    dictionary = load_dictionary("../Exodus/CommandDictionary.txt")
    os.system('./speech.sh What would you like my response to be for ')
    os.system('./speech.sh ' + audioText)
    newResponse = raw_input("What would you like my response to be for (command): ")
    # newResponse = listen()
    dictionary[audioText] = "command_protocols." + newResponse + "()"
    with open("./ResponseDictionary.txt", "r+") as write_file:
        for keys in dictionary.keys():
            print(keys + ":" + dictionary[keys])
            write_file.write(keys + ":" + dictionary[keys])
    os.system('./speech.sh Okay, done!')
    os.system('./speech.sh Please update the code now')



def identifyCommand(command, audioText):
    if (command == "No found responses"):
            os.system('./speech.sh Did not find a response in my database')
            os.system('./speech.sh Please tell me if you would like this to be a command')
            # responseText = listen()
            responseText = raw_input("1: new response 2: command ")
            if responseText.lower() == "new response":
                writeNewResponse(audioText)
            elif responseText.lower() == "command":
                writeNewCommand(audioText)
            else:
               os.system('./speech.sh Okay I wont record a new response')
    elif (command == "None"):
        responseText = "Sorry I couldn't understand that. Can you say that again?"
        os.system('./speech.sh ' + responseText)
    else:
        os.system('./speech.sh ' + command[18:])
        eval(command)
