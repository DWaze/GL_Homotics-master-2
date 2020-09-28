import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)


def change_on():
    print("LED on")
    GPIO.output(24, GPIO.HIGH)


def change_off():
    print("LED off")
    GPIO.output(24, GPIO.LOW)


def destroy():
    GPIO.cleanup()
