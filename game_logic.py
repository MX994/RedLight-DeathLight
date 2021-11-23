from threading import Timer
from random import uniform
from gpio_interface import *
from time import time
from datetime import timedelta

class Game:
    def __init__(self):
        # Initialize GPIO interface.
        self.gpio = RLDL_GPIO()
        # Variables to keep track of the game's state.
        self.isRed = True
        self.gameStarted = False
        self.currentTimer = None
        # Minimum and maximum wait bounds, in seconds.
        self.minWait = 1
        self.maxWait = 10
        # To get time statistics.
        self.startingTime = time()
    
    def __printCurrentLight(self):
        # Swap the state, then print it.
        self.isRed = not self.isRed
        self.currentTimer = None
        print(f'{"Red" if self.isRed else "Green"} Light')

    def start(self):
        # Start game loop.
        self.gameStarted = True
        self.__printCurrentLight()
        self.gpio.changeButtonLightState(self.gameStarted)
        
        while self.gameStarted:
            # Start timer if not already started.
            if self.currentTimer is None:
                # Choose a random value between minWait and maxWait.
                self.currentTimer = Timer(uniform(self.minWait, self.maxWait), self.__printCurrentLight)
                self.currentTimer.start()

            # Check if button was pressed; if so, end the game.
            if self.gpio.getButtonPressed():
                # Button press detected, end game.
                duration = time() - self.startingTime
                self.gameStarted = False
                if self.currentTimer is not None:
                    self.currentTimer.cancel()  
                self.gpio.changeButtonLightState(self.gameStarted)
                self.gpio.deinit()
                print(f'Duration: {str(timedelta(seconds=duration))}')
                
            # Do callback checking here; if movement was detected, send GPIO signals to fire the turret.
            # TODO: Add callback check for movement.
        
        print("Game over!")

