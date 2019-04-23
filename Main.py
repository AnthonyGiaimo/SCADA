import serial
import time


arduino_data = serial.Serial('com4', 9600)

currentTime = time.localtime()
day, year, month, hour, min, sec = currentTime.tm_mday, currentTime.tm_year, currentTime.tm_mon, \
                                   currentTime.tm_hour, currentTime.tm_min, currentTime.tm_sec
end = False

answer = None

while not end:
    currentTime = time.localtime()
    time.sleep(2)
    if arduino_data.read(100) == "clockCheck":
        arduino_data.write(currentTime)

