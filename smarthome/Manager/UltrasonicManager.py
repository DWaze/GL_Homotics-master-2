import time

from smarthome.Driver.UltrasonicDriver import setup, get_distance


class UltrasonicManager:

    def __init__(self):
        setup()

    @staticmethod
    def get_distance():
        try:
            millis = int(round(time.time() * 1000))
            distance_value = get_distance()
            result = '{' \
                     '"Response":' + str(distance_value) + ',' \
                                                           '"Current_time":' + str(millis) + '' \
                                                                                             '}'
            return result
        except ValueError:
            result = '{"Response":"Error"}'
            return result
