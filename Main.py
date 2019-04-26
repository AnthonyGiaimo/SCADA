import serial
import time
import requests
import datetime

# Setup
arduino_data = serial.Serial('com3', 9600)

currentTime = time.localtime()
day, year, month, hour, min, sec = currentTime.tm_mday, currentTime.tm_year, currentTime.tm_mon, \
                                   currentTime.tm_hour, currentTime.tm_min, currentTime.tm_sec
end = False

answer = None

def sessionLoggin():
    username = 'r0lyp0ly'
    password = '300thsquaD*muso'
    remember_me = 'on'
    data = {
        'username':username, 'password':password, 'remember_me':remember_me
    }
    session = requests.session()
    session.post(url="https://tony-giaimo.us/login.php", data=data)
    return session

def getTime(session):
    # api-endpoint
    URL = "https://tony-giaimo.us/coffee.php"

    # user given here

    id = datetime.date(int(year), int(month), int(day)).weekday()

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'day': id}

    # sending post request and saving the response as response object
    response = session.get(url=URL, params=PARAMS)

    # extracting data in json format

    return response.text


session = sessionLoggin()

while not end:
    currentTime = time.localtime()
    day, year, month, hour, min, sec = str(currentTime.tm_mday), str(currentTime.tm_year), str(currentTime.tm_mon), \
                                       str(currentTime.tm_hour), str(currentTime.tm_min), str(currentTime.tm_sec)
    # with the port open, the response will be buffered
    # so wait a bit longer for response here
    # Serial read section

    msg = arduino_data.readline().strip(b'\n').decode()
    print("Message from arduino: ")
    print(msg)
    if msg == "clockCheck":
        arduino_data.write(bytes(hour, 'utf-8'))
        print("wrote to arduino")
    if msg == "alarmSet":
        arduino_data.write(bytes(getTime(session), 'utf-8'))
        print("wrote to arduino")
    if msg == "exit":
        end = True;
    msg = ""
# Close session after done running while loop
session.close()
