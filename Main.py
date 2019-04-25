import serial
import time
import requests
import datetime


arduino_data = serial.Serial('com3', 9600)

end = False

def getTime():
    # api-endpoint
    URL = "https://tony-giaimo.us/coffee.php"
    token = "DogKt8rm6oT5txK6nj6zTMbJV4Wn94fI"

    # user given here

    id = datetime.date(int(year), int(month), int(day)).weekday()

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'day': id, 'auth': token}

    # sending post request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format

    return r.text


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
        arduino_data.write(bytes(getTime(), 'utf-8'))
        print("wrote to arduino")
    msg = ""
