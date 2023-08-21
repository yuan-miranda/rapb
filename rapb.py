import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)

def turn_on_bulb():
    ser.write(b'1')
    print("bulb turned on")
def turn_off_bulb():
    ser.write(b'0')
    print("buld turned off")

while True:
    user_input = input("on/off/exit:")
    if user_input == 'on':
        turn_on_bulb()
    elif user_input == 'off':
        turn_off_bulb()
    elif user_input == 'exit':
        break
    else:
        print("invalid input")

ser.close()