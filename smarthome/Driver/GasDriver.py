#!/usr/bin/env python
import smarthome.Driver.PCF8591 as ADC
import RPi.GPIO as GPIO

DO = 6
GPIO.setmode(GPIO.BCM)


def setup():
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)


def get_gaz():
    gaz_value = ADC.read(0)
    return gaz_value


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        setup()
        get_gaz()
    except KeyboardInterrupt:
        destroy()
