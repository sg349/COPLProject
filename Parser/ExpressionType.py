from enum import Enum

# Coogan Koerts, Brent Einolf, Sam Gardiner

# This is an enum class that is used to determine which type of expression is being used.

class ExpressionType(Enum):
    BOOLEAN = 1
    ARITHMETIC = 2
    ASSIGNMENT = 3
