from enum import Enum


class StatementType(Enum):
    ARITHMETIC = 1
    IF = 2
    ASSIGNMENT = 3
    WHILE = 4
    REPEAT = 5
    FOR = 6
    PRINT = 7

    def string_type(self):
        if self.value == 1:
            return "arithmetic_statement"

        if self.value == 2:
            return "if_statement"

        if self.value == 3:
            return "assignment_statement"

        if self.value == 4:
            return "while_statement"

        if self.value == 5:
            return "repeat_statement"

        if self.value == 6:
            return "for_statement"

        if self.value == 7:
            return "print_statement"
