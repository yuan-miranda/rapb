import serial

# Change "COM3" based on what port your using
ser = serial.Serial("COM3", 9600, timeout=1)

def turnOffCharger(): # Turn off the relay
    ser.write(b'0')

def turnOnCharger():  # Turn on the relay
    ser.write(b'1')

def fetchStatus():    # Get the relay status
    ser.write(b'2')
    print(ser.readline().decode().strip())

# Upcoming shortcut (concept):
# off         0
# on          1
# status  sts 2
# restart res 3
# exit    ext 4

while True:
    # Get user input
    user_input = input("rapb.py $: ")
    
    if user_input == "on":
        turnOnCharger()
    elif user_input == "off":
        turnOffCharger()
    elif user_input == "status":
        fetchStatus()
    elif user_input == "restart":
        turnOffCharger() # LMAO
    elif user_input == "exit":
        break
    else:
        print("invalid input")

ser.close()