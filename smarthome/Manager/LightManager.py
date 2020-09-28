from smarthome.Driver.LightDriver import change_on, change_off, setup, destroy
import time


class LightManager(object):

    def __init__(self):
        setup()

    @staticmethod
    def light_on():
        try:
            millis = int(round(time.time() * 1000))
            change_on()
            result = '{' \
                     '"Response":"Light on",' \
                     '"Current_time":' + str(millis) + '' \
                                                       '}'
            return result

        except ValueError:
            result = '{"Response":"Error"}'
            return result

    @staticmethod
    def light_off():
        try:
            millis = int(round(time.time() * 1000))
            change_off()
            result = '{' \
                     '"Response":"Light on",' \
                     '"Current_time":' + str(millis) + '' \
                                                       '}'
            return result

        except ValueError:
            result = '{"Response":"Error"}'
            return result

    @staticmethod
    def clean_gpio():
        destroy()

