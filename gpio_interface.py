import RPi.GPIO as GPIO
import asyncio

class RLDL_GPIO:
    def __init__(self):
        self.outputPins = {
            'triggerRelay' : 23,
            'motorRelay' : 24,
            'neopixelGrid' : 25,
        }
        self.inputPins = {
            'buttonPin' : 22,
        }
        for pin in self.outputPins:
            GPIO.setup(self.outputPins[pin], GPIO.OUT)
        for pin in self.inputPins:
            GPIO.setup(self.inputPins[pin], GPIO.IN)
    
    async def fire_nerf_gun(self):
        # Spin motor, fire, stop spinning.
        GPIO.output(self.outputPins['motorRelay'], GPIO.HIGH)
        await asyncio.sleep(1)
        GPIO.output(self.outputPins['triggerRelay'], GPIO.HIGH)
        await asyncio.sleep(0.4)
        GPIO.output(self.outputPins['triggerRelay'], GPIO.LOW)
        GPIO.output(self.outputPins['motorRelay'], GPIO.LOW)

    async def change_light_pattern(self):
        # TODO: Implement stop light pattern.
        return

    async def play_sound(self):
        # TODO: Play sound through speakers.
        return


