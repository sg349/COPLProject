from enum import Enum


class WordType(Enum):
    KEYWORD = 1
    OPERATOR = 2
    NUMBER = 3
    IDENTIFIER = 4
    SYMBOL = 5
    NEWLINE = 6

    def string_type(self, to_print_id):
        if to_print_id == 2:
            return "operator"

        if to_print_id == 3:
            return "integer_literal"

        if to_print_id == 4:
           return "identifier"
