import RPi.GPIO as GPIO
from time import sleep
import board
import neopixel

class GPIOInterface:
	def __init__(self):
		self.outputPins = {
			'buttonLight' : 22,
			'servo' : 19,
		}
		self.inputPins = {
			'buttonPin' : 10,
		}
		self.states = {
			'buttonLight' : False,
			'redLight': True,
		}
		self.neoPixel = neopixel.NeoPixel(board.D18, 256, brightness=0.1)
		GPIO.setmode(GPIO.BCM)
		for pin in self.outputPins:
			GPIO.setup(self.outputPins[pin], GPIO.OUT)
		for pin in self.inputPins:
			GPIO.setup(self.inputPins[pin], GPIO.IN)
		self.servo = GPIO.PWM(self.outputPins['servo'], 50)
		self.servo.start(0)
	
	def setServoAngle(self, angle):
		duty = angle / 180
		GPIO.output(self.outputPins['servo'], True)
		self.servo.ChangeDutyCycle(duty)
		sleep(1)
		GPIO.output(self.outputPins['servo'], False)
		self.servo.ChangeDutyCycle(0)		

	def changeState(self, key):
		if key in self.states.keys():
			self.states[key] = not self.states[key]
			GPIO.output(self.outputPins[key], self.states[key])
		else:
			print(f'Unknown key {key}!')
		return

	def changeButtonLightState(self):
		self.changeState('buttonLight')

	def getButtonPressed(self):
		print(GPIO.input(self.inputPins['buttonPin']))
		return GPIO.input(self.inputPins['buttonPin'])	

	def getButtonLightState(self):
		return self.states['buttonLight']	

	def getRedLightState(self):
		return self.states['redLight']		

	def deinit(self):
		GPIO.cleanup()

	def changeLightColor(self):
		self.states['redLight'] = not self.states['redLight']
		self.neoPixel.fill((255, 0, 0)) if self.getRedLightState() else self.neoPixel.fill((0, 255, 0)) 
		self.neoPixel.show()
		return
		
	def playSound(self):
		# TODO: Play sound through speakers.
		return


