import serial

# Change "COM3" based on what USB port your using for Arduino
ser = serial.Serial("COM3", 9600, timeout=1)

def turn_on():  # Turn on the relay
    ser.write(b'1')

def turn_off(): # Turn off the relay
    ser.write(b'0')

def get_status(): # Get the relay status
    ser.write(b'2')
    print(ser.readline().decode().strip())

def help():
    print("""Remote Accessed Power Brick (RAPB)
Control the power brick (laptop charger) remotely using Arduino and a relay module via serial communication interface.
Commands and Shortcuts:
on,            1 : Turn on the relay
off,           0 : Turn off the relay
status,  sts,  2 : Get the relay status
restart, res,  3 : Verbosed version of "off" command lol
exit,    quit, q : Exit the script
help,          h : Print the help page""")

while True:
    # Get user input
    user_input = input("rapb.py: ")
    
    if user_input in ["on", '1']:
        turn_on()

    elif user_input in ["off",'0']:
        turn_off()

    elif user_input in ["status", "sts", '2']:
        get_status()

    elif user_input in ["restart", "res", "3"]:
        turn_off() # LMAO

    elif user_input in ["exit", "quit", 'q']:
        break

    elif user_input in ["help", 'h']:
        help()

    else:
        print("invalid command")

ser.close()