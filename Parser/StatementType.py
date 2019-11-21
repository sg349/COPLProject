from enum import Enum

# Coogan Koerts, Brent Einolf, Sam Gardiner

# This is an enum class that is used to determine which type of statement is being used.


class StatementType(Enum):
    ELSE = 1
    CONDITIONAL = 2
    ASSIGNMENT = 3
    WHILE = 4
    REPEAT = 5
    FOR = 6
    PRINT = 7

    def string_type(self):
        if self.value == 1:
            return "else_statement"

        if self.value == 2:
            return "conditional_statement"

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
