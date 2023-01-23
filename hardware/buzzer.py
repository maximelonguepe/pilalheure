import RPi.GPIO as GPIO
import gpiozero

triggerPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN, GPIO.OUT)
buzzer = gpiozero.Buzzer(21)
print("test")
buzzer.on()
