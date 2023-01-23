import RPi.GPIO as GPIO
import gpiozero

triggerPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN, GPIO.OUT)
buzzer = gpiozero.Buzzer(21)


def buzz_on():
    buzzer.on()


def buzz_off():
    buzzer.off()
