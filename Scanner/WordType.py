from enum import Enum


class WordType(Enum):
    KEYWORD = 1
    OPERATOR = 2
    NUMBER = 3
    IDENTIFIER = 4
    SYMBOL = 5
    NEWLINE = 6

    def string_type(self):
        if self.value == 2:
            return "operator"

        if self.value == 3:
            return "integer_literal"

        if self.value == 4:
            return "identifier"