from enum import Enum

# Coogan Koerts, Brent Einolf, Sam Gardiner

# This is an enum class that is used to determine which type of Operator is being used.

class OperatorType(Enum):
    ARITHMETIC = 1
    RELATIVE = 2
    ASSIGNMENT = 3
