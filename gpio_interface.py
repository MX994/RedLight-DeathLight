import RPi.GPIO as GPIO
from time import sleep

class RLDL_GPIO:
	def __init__(self):
		self.outputPins = {
			'buttonLight' : 22,
			'triggerRelay' : 23,
			'motorRelay' : 24,
			'neopixelGrid' : 25,
		}
		self.inputPins = {
			'buttonPin' : 10,
		}
		self.states = {
			'buttonLight' : False,
			'motorRelay' : False,
			'triggerRelay' : False,
		}
		GPIO.setmode(GPIO.BCM)
		for pin in self.outputPins:
			GPIO.setup(self.outputPins[pin], GPIO.OUT)
		for pin in self.inputPins:
			GPIO.setup(self.inputPins[pin], GPIO.IN)
	
	def changeState(self, key, newState, value):
		if key in self.states.keys():
			self.states[key] = newState
			GPIO.output(self.outputPins[key], value)
		else:
			print(f'Unknown key {key}!')
		return

	def changeButtonLightState(self, state):
		self.changeState('buttonLight', state, state)

	def changeMotorState(self, state):
		self.changeState('motorRelay', state, not state)

	def changeTriggerState(self, state):
		self.changeState('triggerRelay', state, not state)

	def getButtonPressed(self):
		return not GPIO.input(self.inputPins['buttonPin'])

	def getMotorState(self):
		return self.states['motorRelay']

	def getTriggerState(self):
		return self.states['triggerRelay']	

	def getButtonLightState(self):
		return self.states['buttonLight']	

	def deinit(self):
		GPIO.cleanup()

	def changeLightColor(self):
		# TODO: Implement stop light pattern.
		return

	def playSound(self):
		# TODO: Play sound through speakers.
		return


