from enum import Enum


class SymbolType(Enum):
    LETTER = 1
    NUMBER = 2
    OPERATOR = 3
    NEWLINE = 4
    SPACE = 5
    SYMBOL = 6


class WordType(Enum):
    KEYWORD = 1
    OPERATOR = 2
    NUMBER = 3
    IDENTIFIER = 4
    SYMBOL = 5
    NEWLINE = 6

