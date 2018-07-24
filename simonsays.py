import RPi.GPIO as GPIO
import LEDRGB as LED
import time 
import random
# this script blinks one of four random colors on the
colors =['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
# this script plays one of four random notes ob the passive buzzer
# breadboardsetup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)
frequences = [220, 440, 880, 1760]

def loop():
	n = random.randint(0,3)
	color_sequence = [colors[n]]
	while True:
		for i in range(0, len(color_sequence)):
			Buzz.ChangeFrequency(frequencies[n])
			Buzz.start(50)
			time.sleep(0.5)
			LED.setColor(color_sequence[n])
			Buzz.stop()
			time.sleep(0.5)
			LED.noColor()
			time.sleep(0.2)
		n = random.randint(0,3)
		color_sequence. append(colors[n])
		time.sleep(0.3)
if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:		
		print 'Good bye'
		LED.destroy()
