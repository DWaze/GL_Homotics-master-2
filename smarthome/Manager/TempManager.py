import time

from smarthome.Driver.TempDriver import setup, get_temp


class TempManager:

    def __init__(self):
        setup()

    @staticmethod
    def get_temp():
        try:
            millis = int(round(time.time() * 1000))
            tem_value = get_temp()
            result = '{' \
                     '"Response":' + str(tem_value) + ',' \
                                                      '"Current_time":' + str(millis) + '' \
                                                                                        '}'
            return result
        except ValueError:
            result = '{"Response":"Error"}'
            return result
