from Scanner.WordType import WordType
from Parser.OperatorType import OperatorType


class Token:
    def __init__(self, enum_type, id, value):
        self.enum_type = enum_type
        self.id = id
        self.value = value
        if enum_type == WordType.OPERATOR:
            if id == 0:
                self.operator_type = OperatorType.ASSIGNMENT
            elif id <= 6:
                self.operator_type = OperatorType.RELATIVE
            else:
                self.operator_type = OperatorType.ARITHMETIC

    def print_token(self):
        print("<" + WordType.string_type(self.enum_type) + " " + " id:" + str(self.id) + "> -> " + str(self.value))
