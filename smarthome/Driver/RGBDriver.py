import time

import RPi.GPIO as GPIO
import sys
import logging
import traceback

R = 19
G = 26
B = 27


def setup():
    global pins
    global p_R, p_G, p_B
    pins = {'pin_R': R, 'pin_G': G, 'pin_B': B}
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)  # Set pins' mode is output
        GPIO.output(pins[i], GPIO.HIGH)  # Set pins to high(+3.3V) to off led

    p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
    p_G = GPIO.PWM(pins['pin_G'], 2000)
    p_B = GPIO.PWM(pins['pin_B'], 2000)

    p_R.start(0)  # Initial duty Cycle = 0(leds off)
    p_G.start(0)
    p_B.start(0)


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def off():
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)  # Turn off all leds


def setColor(col):  # For example : col = 0x112233
    R_val = (col & 0x110000) >> 16
    G_val = (col & 0x001100) >> 8
    B_val = (col & 0x000011) >> 0

    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(100 - R_val)  # Change duty cycle
    p_G.ChangeDutyCycle(100 - G_val)
    p_B.ChangeDutyCycle(100 - B_val)


def change_color(col):
    setColor(col)


def destroy():
    GPIO.cleanup()


def change_clr(col):
    try:
        col = int('0x' + col, 16)
        change_color(col)
        return '{"responce":"Color Changed successfully"}'
    except Exception as e:
        logging.error(traceback.format_exc())
        print(e)
        destroy()
