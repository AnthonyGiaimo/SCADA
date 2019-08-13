import subprocess
import os
import Command_Library

def printTest():
    print("Hello World")

def good4di(option):
    if option == 0:
        print("This will be the sign form 1 command")
    elif option == 1:
        print("This will be the sign in command")
    elif option == 2:
        print("This will be the sign out command")
        
def internet():
    os.system('ping -c 1 www.google.com | ./speech.sh') # Will give me status of the internet

def coffe(option):
    if option == 0:
        print("This will be the stop brewing command")
    elif option == 1:
        print("This will be the brew command")
    elif option == 2:
        print("This will be the set alarm command")
