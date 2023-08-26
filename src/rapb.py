import serial

# Change "COM3" based on what USB port your using for Arduino
ser = serial.Serial("COM3", 9600, timeout=1)

def turnOnCharger():  # Turn on the relay
    ser.write(b'1')

def turnOffCharger(): # Turn off the relay
    ser.write(b'0')

def fetchStatus():    # Get the relay status
    ser.write(b'2')
    print(ser.readline().decode().strip())

# Read this as "if command in input is in the selection"
def command(input, selection=[]):
    for option in selection:
        if input == option:
            return True
    return False

def help():
    print("""Remote Access Power Brick (RAPB)
Control the power brick (laptop charger) remotely using Arduino and a relay module using serial communication interface.
Commands and Shortcuts:
on,            1 : Turn on the relay
off,           0 : Turn off the relay
status,  sts,  2 : Get the relay status
restart, res,  3 : Verbosed version of "off" command lol
exit,    quit, q : Exit the script
help,          h : Print the help page""")

while True:
    # Get user input
    userInput = input("rapb.py: ")
    
    if command(userInput, ["on", '1']):
        turnOnCharger()
    elif command(userInput, ["off",'0']):
        turnOffCharger()
    elif command(userInput, ["status", "sts", '2']):
        fetchStatus()
    elif command(userInput, ["restart", "res", '3']):
        turnOffCharger() # LMAO
    elif command(userInput, ["exit", "quit", 'q']):
        break
    elif command(userInput, ["help", 'h']):
        help()
    else:
        print("invalid command")

ser.close()