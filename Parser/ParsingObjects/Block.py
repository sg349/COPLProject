from Scanner.WordType import WordType
from Parser.ParsingObjects.Statement import Statement
from Parser.StatementType import StatementType


class Block:
    blocks = []
    statements = []

    def __init__(self, start_index, end_index, collection):
        self.start_index = start_index
        self.end_index = end_index
        self.collection = collection

    def evaluate_block(self):
        while True:
            if self.collection[self.start_index][0].type == WordType.KEYWORD and self.collection[self.start_index][0].id == 7:
                break
            # Statement
            elif self.collection[self.start_index][0].type == WordType.KEYWORD:
                print("tbd")
            # Assignment Statement
            elif self.collection[self.start_index][0].type == WordType.IDENTIFIER:
                assignment_statement = Statement(self.collection[self.start_index], StatementType.ASSIGNMENT)
                self.statements.append(assignment_statement)
