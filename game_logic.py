from threading import Timer
from random import uniform
from GPIOInterface import *
from ESP32Interface import * 
from time import time
from datetime import timedelta
from CameraInterface import *

class Game:
    def __init__(self):
        # Initialize GPIO interface.
        self.gpio = GPIOInterface()
        self.cam = CameraInterface()
        self.esp32 = ESP32Communication()
        # Variables to keep track of the game's state.
        self.isRed = True
        self.gameStarted = False
        self.currentTimer = None
        # Minimum and maximum wait bounds, in seconds.
        self.minWait = 0.5
        self.maxWait = 3.5
        # To get time statistics.
        self.startingTime = time()
        self.frameCounter = 0
    
    def __printCurrentLight(self):
        # Swap the state, then print it.
        self.isRed = not self.isRed
        self.gpio.changeLightColor()
        self.currentTimer = None
        print(f'{"Red" if self.isRed else "Green"} Light')

    def start(self):
        # Start game loop.
        self.gameStarted = True
        self.__printCurrentLight()
        self.gpio.changeButtonLightState()
        
        while self.gameStarted:
            # Start timer if not already started.
            if self.currentTimer is None:
                # Choose a random value between minWait and maxWait.
                self.currentTimer = Timer(uniform(self.minWait, self.maxWait), self.__printCurrentLight)
                self.currentTimer.start()

            # Check if button was pressed; if so, end the game.
            if self.gpio.getButtonPressed() :
                # Button press detected, end game.
                duration = time() - self.startingTime
                self.gameStarted = False
                if self.currentTimer is not None:
                    self.currentTimer.cancel()  
                self.gpio.changeButtonLightState()
                self.gpio.clearNeopixel()
                self.gpio.deinit()
                print(f'Duration: {str(timedelta(seconds=duration))}')    
                
            # Do callback checking here; if movement was detected, send GPIO signals to fire the turret.
            if self.gpio.getRedLightState():
                self.cam.trackingMovement()
                if self.cam.getFoundMovement() and self.frameCounter > 10:
                    self.esp32.fire(1)
                    self.cam.resetFoundMovement()
                    self.frameCounter = 0
                self.frameCounter += 1
            else:
                self.frameCounter = 0
        
        print("Game over!")

