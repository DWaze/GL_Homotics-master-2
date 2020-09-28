import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)


def motor_status_on():
    # p = GPIO.PWM(5, 207)
    # p.start(0)
    try:
        GPIO.output(5, GPIO.LOW)
        # p.ChangeDutyCycle(15)
        time.sleep(6)
        GPIO.output(5, GPIO.HIGH)
        # p.ChangeDutyCycle(100)
        # time.sleep(3)
    except KeyboardInterrupt:
        pass
    # p.stop()
    # GPIO.cleanup()


def motor_status_off():
    # p = GPIO.PWM(5, 207)
    # p.start(0)
    try:
        GPIO.output(5, GPIO.HIGH)
        # p.ChangeDutyCycle(100)
    except KeyboardInterrupt:
        pass
    # p.stop()
    # GPIO.cleanup()
