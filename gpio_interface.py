import RPi.GPIO as GPIO
from time import sleep
import board
import neopixel

class RLDL_GPIO:
	def __init__(self):
		self.outputPins = {
			'buttonLight' : 22,
			'triggerRelay' : 23,
			'motorRelay' : 24,
		}
		self.inputPins = {
			'buttonPin' : 10,
		}
		self.states = {
			'buttonLight' : False,
			'motorRelay' : False,
			'triggerRelay' : False,
			'redLight': True,
		}
		self.neoPixel = neopixel.NeoPixel(board.D18, 256, brightness=0.1)
		GPIO.setmode(GPIO.BCM)
		for pin in self.outputPins:
			GPIO.setup(self.outputPins[pin], GPIO.OUT)
		for pin in self.inputPins:
			GPIO.setup(self.inputPins[pin], GPIO.IN)
	
	def changeState(self, key, newState, value, fn):
		if key in self.states.keys():
			self.states[key] = newState
			fn(value, key)
		else:
			print(f'Unknown key {key}!')
		return

	def changeButtonLightState(self, state):
		self.changeState('buttonLight', state, state, lambda x, y: GPIO.output(self.outputPins[y], x))

	def changeMotorState(self, state):
		self.changeState('motorRelay', state, lambda x, y: GPIO.output(self.outputPins[y], x))

	def changeTriggerState(self, state):
		self.changeState('triggerRelay', state, lambda x, y: GPIO.output(self.outputPins[y], x))

	def getButtonPressed(self):
		return not GPIO.input(self.inputPins['buttonPin'])

	def getMotorState(self):
		return self.states['motorRelay']

	def getTriggerState(self):
		return self.states['triggerRelay']	

	def getButtonLightState(self):
		return self.states['buttonLight']	

	def getRedLightState(self):
		return self.states['redLight']		

	def deinit(self):
		GPIO.cleanup()

	def changeLightColor(self, state):
		self.changeState('redLight', state, state, 
		lambda x, y: self.neoPixel.fill((0x0, 0xFF, 0x0) 
			if not self.getRedLightState() 
			else (0xFF, 0x0, 0x0)))
		

	def playSound(self):
		# TODO: Play sound through speakers.
		return


