"""
This is the python file that holds all of the commands for Exodus to use.
"""

import pyttsx3
import speech_recognition as sr
import command_protocols


def initialize():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say("Hello Tony. Please wiat while I get a few things ready for you.")
    engine.say("Okay, all ready. How may I help you today?")
    engine.runAndWait()
    return engine


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
    social_dictionary = load_dictionary("../Exodus/ResponseDictionary.txt")
    command_dictionary = load_dictionary("../Exodus/CommandDictionary.txt")
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


def writeNewResponse(audioText, engine):
    dictionary = load_dictionary("../Exodus/ResponseDictionary.txt")
    engine.say("What would you like my response to be for ")
    engine.say(audioText)
    engine.runAndWait()
    newResponse = input("What would you like me to say (social): ")
    # newResponse = listen()
    dictionary[audioText] = newResponse
    with open("../Exodus/ResponseDictionary.txt", "r+") as write_file:
        for keys in dictionary.keys():
            print(keys + ":" + dictionary[keys])
            print(keys + ":" + dictionary[keys], end="\n", file=write_file)
    engine.say("Okay, done!")
    engine.runAndWait()


def writeNewCommand(audioText, engine):
    dictionary = load_dictionary("../Exodus/CommandDictionary.txt")
    engine.say("What would you like my response to be for ")
    engine.say(audioText)
    engine.runAndWait()
    newResponse = input("What would you like my response to be for (command): ")
    # newResponse = listen()
    dictionary[audioText] = "command_protocols." + newResponse + "()"
    with open("../Exodus/ResponseDictionary.txt", "r+") as write_file:
        for keys in dictionary.keys():
            print(keys + ":" + dictionary[keys])
            print(keys + ":" + dictionary[keys], end="\n", file=write_file)
    engine.say("Okay, done!")
    engine.say("Please update the code now.")
    engine.runAndWait()



def identifyCommand(command, engine, audioText):
    if (command == "No found responses"):
            engine.say("Did not find a response in my database.")
            engine.say("Please tell me if you would like this to be a command.")
            engine.runAndWait()
            # responseText = listen()
            responseText = input("Please tell me if you would like this to be a command: ")
            if responseText.lower() == "new response":
                writeNewResponse(audioText, engine)
            elif responseText.lower() == "command":
                writeNewCommand(audioText, engine)
            else:
                engine.say("Okay I won't record a new response.")
                engine.runAndWait()
    elif (command == "None"):
        responseText = "Sorry I couldn't understand that. Can you say that again?"
        engine.say(responseText)
        engine.runAndWait()
    else:
        engine.say(command[18:])
        eval(command)
