from enum import Enum


class StatementType(Enum):
    ARITHMETIC = 1
    IF = 2
    ASSIGNMENT = 3
    WHILE = 4
    REPEAT = 5
    FOR = 6
