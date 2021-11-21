from threading import Timer
from random import uniform

class Game:
    def __init__(self):
        # Variables to keep track of the game's state.
        self.isRed = True
        self.gameStarted = False
        self.currentTimer = None
        # Minimum and maximum wait bounds, in seconds.
        self.minWait = 1
        self.maxWait = 3
    
    def __printCurrentLight(self):
        # Swap the state, then print it.
        self.isRed = not self.isRed
        self.currentTimer = None
        print(f'{"Red" if self.isRed else "Green"} Light')

    def start(self):
        # Start game loop.
        self.gameStarted = True
        self.__printCurrentLight()
        
        while self.gameStarted:
            # Start timer if not already started.
            if self.currentTimer is None:
                # Choose a random value between minWait and maxWait.
                self.currentTimer = Timer(uniform(self.minWait, self.maxWait), self.__printCurrentLight)
                self.currentTimer.start()
            
            # Do callback checking here; if movement was detected, send GPIO signals to fire the turret.
            # TODO: Add callback check for movement.

            # Check if button was pressed; if so, end the game.
            # TODO: Add button press check.
