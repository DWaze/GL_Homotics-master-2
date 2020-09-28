import time

from smarthome.Driver.RGBDriver import setup, change_clr, destroy


class RGBManager:

    def __init__(self):
        # destroy()
        setup()

    @staticmethod
    def rgb_change(color):
        try:
            millis = int(round(time.time() * 1000))
            change_clr(color)
            result = '{' \
                     '"Response":"Color Changed",' \
                     '"Current_time":' + str(millis) + '' \
                                                       '}'
            return result
        except ValueError:
            result = '{"Response":"Error"}'
            return result

    @staticmethod
    def rgb_off():
        try:
            millis = int(round(time.time() * 1000))
            change_clr("000000")
            result = '{' \
                     '"Response":"RGB Off",' \
                     '"Current_time":' + str(millis) + '' \
                                                       '}'
            return result

        except ValueError:
            result = '{"Response":"Error"}'
            return result
