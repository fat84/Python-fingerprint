import serial                                                              #Serial imported for Serial communication
import time                                                                #Required to use delay functions
import struct

def enrollFinger(id):
    arduino = serial.Serial('/dev/ttyUSB0', 9600,
                            timeout=.1)  # Create Serial port object called ArduinoUnoSerialData time.sleep(2)                                                             #wait for 2 secounds for the communication to get established
    time.sleep(2)  # give the connection a second to settle
    loop = True
    arduino.write(struct.pack('>B', 1))
    time.sleep(1)
    arduino.write(struct.pack('>B', id))
    while(loop):
        data = arduino.readline()
        data = str(data)
        if (data == "successful\r\n"):
            print arduino.readline()
            loop = False
        if (data == 'c\r\n'):
            return "Failed"
    return id

def clockIn(id):
    arduino = serial.Serial('/dev/ttyUSB0', 9600,
                            timeout=.1)  # Create Serial port object called ArduinoUnoSerialData time.sleep(2)                                                             #wait for 2 secounds for the communication to get established
    time.sleep(2)  # give the connection a second to settle
    loop = True
    arduino.write(struct.pack('>B', 2))
    time.sleep(1)
    arduino.write(struct.pack('>B', id))
    while(loop):
        data = arduino.readline()
        data = str(data)
        if (data == "matched\r\n"):
            score = arduino.readlines()
            loop = False
        if (data == 'c\r\n'):
            return 0
    return score

def compareCharacteristic(finger1,finger2):
    finger1 = str(finger1).split(",")
    finger2 = str(finger2).split(",")
    if(len(finger1) > len(finger2)):
        count = 0
        result = 0
        notEqual = 0
        while(len(finger2) > count):
            if(finger1[count] == finger2[count]):
                result += 1
            if (finger1[count] != finger2[count]):
                notEqual += 1
            count+= 1
    if(len(finger2) > len(finger1)):
        count = 0
        result = 0
        notEqual = 0
        while (len(finger1) > count):
            if (finger1[count] == finger2[count]):
                result += 1
            if (finger1[count] != finger2[count]):
                notEqual += 1
            count += 1
    if (len(finger2) == len(finger1)):
        count = 0
        result = 0
        notEqual = 0
        while (len(finger1) > count):
            if (finger1[count] == finger2[count]):
                result += 1
            if (finger1[count] != finger2[count]):
                notEqual += 1
            count += 1
    return result - notEqual

