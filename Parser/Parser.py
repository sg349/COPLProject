from Scanner.WordType import WordType
from Parser.ParsingObjects.Block import Block

# Coogan Koerts, Brent Einolf, Sam Gardiner

# This is the actual Parser class that drives the parsing of the tokens scanned in from the Scanner. The Block method
# is a recursive method that will continue to call itself until all statements have been called.


class Parser:
    line_collection = []

    def __init__(self, line_collection):
        Parser.line_collection = line_collection
        self.start_block = []

    def parse(self):
        if self.line_collection[0][0].enum_type != WordType.KEYWORD or self.line_collection[0][0].id != 3:
            raise Exception("Expected Function at start of file")

        self.start_block = Block(self.line_collection)
        self.start_block.evaluate_block(False)
        self.print_parse(self.start_block)
        return self.start_block

    def print_parse(self, start):
        print("function " + self.line_collection[0][1].value + "( ) <block> end")
        start.print_block()
