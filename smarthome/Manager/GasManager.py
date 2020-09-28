import time

from smarthome.Driver.GasDriver import setup, get_gaz


class GasManager:

    def __init__(self):
        setup()

    @staticmethod
    def get_gaz_value():
        try:
            millis = int(round(time.time() * 1000))
            tem_value = get_gaz()
            result = '{' \
                     '"Response":' + str(tem_value) + ',' \
                                                      '"Current_time":' + str(millis) + '' \
                                                                                        '}'
            return result
        except ValueError:
            result = '{"Response":"Error"}'
            return result
