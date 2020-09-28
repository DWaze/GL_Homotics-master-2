import sys
import time
import logging


from smarthome.Driver.MotorDriver import motor_status_on, motor_status_off, setup


class MotorManager:

    def __init__(self):
        setup()

    @staticmethod
    def motor_on():
        try:
            millis = int(round(time.time() * 1000))
            motor_status_on()
            result = '{' \
                     '"Response":"Motor on",' \
                     '"Current_time":' + str(millis) + '' \
                                                       '}'
            return result

        except:
            print("Unexpected error", sys.exc_info()[0])
            result = '{"Response":"Error"}'
            return result

    @staticmethod
    def motor_off():
        try:
            millis = int(round(time.time() * 1000))
            motor_status_off()
            result = '{' \
                     '"Response":"Motor off",' \
                     '"Current_time":' + str(millis) + '' \
                                                       '}'
            return result

        except ValueError:
            result = '{"Response":"Error"}'
            return result
