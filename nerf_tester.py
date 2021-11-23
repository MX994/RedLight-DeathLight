# A rudimentary fire mechanics tester.

from gpio_interface import *

c = RLDL_GPIO()

def print_usage():
    print(('NERF Ultra Select Tester ~ Usage:\n'
    'm ~ toggles motor on/off (changes state).\n'
    'f ~ fires trigger.\n'
    'x ~ terminates program. Will free GPIO.\n'
    'h ~ hello (shows this).\n'))
print_usage()
while True:
    var = input("Give me a command: ")
    # No switch cases in Python 3.7.
    if var.lower() == 'm':
        # Toggle motor ON/OFF.
        c.changeMotorState(not c.getMotorState())
        print(f'Motor: {"ON" if c.getMotorState() else "OFF"}')
    elif var.lower() == 'f':
        # ON, delay for 200 milliseconds (blocking), OFF.
        if c.getMotorState():
            print(f'Ready... Aim... Fire!')
            c.changeTriggerState(not c.getTriggerState())
            sleep(0.2)
            c.changeTriggerState(not c.getTriggerState())
        else:
            print('Send command \'M\' to turn on the motor, first!')
    elif var.lower() == 'x':
        # Terminate program.
        if c.getMotorState():
            c.changeMotorState(not c.getMotorState())
        if c.getTriggerState():
            c.changeTriggerState(not c.getTriggerState())
        c.deinit() # Free GPIO for other program usage.
        print(f'Exiting...')
        break
    elif var.lower() == 'h':
        print_usage()
    else:
        print('Invalid command. Type \'h\' for details.')