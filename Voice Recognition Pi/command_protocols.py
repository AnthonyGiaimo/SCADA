import subprocess
import os

import Command_Library


def printTest():
    print("Hello World")


def openProgram(program):
    program = program.lower()
    pathDict = Command_Library.load_dictionary("../Exodus/ResponseDictionary.txt")
    if program == "calculator":
        program = "calc"
    programPath = find(program + ".exe", "C:\\")
    if programPath != None:
        os.startfile(programPath)
    else:
        print("No such program exists I'm sorry")

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)



