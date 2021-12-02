# A rudimentary fire mechanics tester.

from ESP32Interface import *
from GPIOInterface import *

c = ESP32Communication()
g = GPIOInterface()

def print_usage():
    print(('NERF Ultra Select Tester ~ Usage:\n'
    'f ~ fires.\n'
    'x ~ terminates program. Will free GPIO.\n'
    'h ~ hello (shows this).\n'))

print_usage()

while True:
    var = input("Give me a command: ")
    # No switch cases in Python 3.7.
    if var.lower() == 'f':
        # Let the ESP32 handle it. :)
        c.fire(int(input('How many times? ')))
    elif var.lower() == 'x':
        print("Peace.")
        exit()
    elif var.lower() == 's':
        angle = int(input('Angle? '))
        print(f'Servo angle set: {angle}')
        g.setServoAngle(angle)
    elif var.lower() == 'h':
        print_usage()
    else:
        print('Invalid command. Type \'h\' for details.')