""" Class for additional Digit """
import datetime


class AddDigit:
    value = 0
    description = ""
    position = 0

    def __init__(self, positon=0):
        self.value = datetime.datetime.today()
        self.position = positon
        self.description = "AD"

    # init def

    def set_add_digit(self, value, position, description):
        self.value = value
        self.position = position
        self.description = description
        pass
    # set_add_digit def

    def get_add_digit(self):
        return self
        pass
    # get_add_digit def

    def get_value(self):
        return self.value
        pass
    # get_value def

    def get_description(self):
        return self.description
        pass
    # get_description def

    def get_position(self):
        return self.position
        pass
    # get_position def

# AddDigit class
