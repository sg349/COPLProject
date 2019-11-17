from Scanner.WordType import WordType
from Parser.ParsingObjects.Statement import Statement
from Parser.StatementType import StatementType


# how the evaluate_block

class Block:

    def __init__(self, start_index, end_index, collection):
        self.start_index = start_index
        self.end_index = end_index
        self.collection = collection
        self.curr_index = 0
        self.statements = []

    def evaluate_block(self):
        self.curr_index = self.start_index
        while self.curr_index != self.end_index:
            # if self.collection[self.curr_index][0].enum_type == WordType.KEYWORD and self.collection[self.curr_index][0].id == 7:
            #     break
            # Keyword Statement
            if self.collection[self.curr_index][0].enum_type == WordType.KEYWORD:
                # conditional statement
                if self.collection[self.curr_index][0].id == 0:
                    self.statements.append(Statement(self.collection[self.curr_index], StatementType.CONDITIONAL))
                    block_end_index = self.find_end()
                    statement_block = Block(self.curr_index + 1, block_end_index, self.collection)
                    statement_block.evaluate_block()

                # while statement
                elif self.collection[self.curr_index][0].id == 1:
                    self.statements.append(Statement(self.collection[self.curr_index], StatementType.WHILE))
                    block_end_index = self.find_end()
                    statement_block = Block(self.curr_index + 1, block_end_index, self.collection)
                    statement_block.evaluate_block()

                # print statement
                elif self.collection[self.curr_index][0].id == 7:
                    self.statements.append(Statement(self.collection[self.curr_index], StatementType.PRINT))
                    statement_block = Block(self.curr_index + 1, self.curr_index + 1, self.collection)
                    statement_block.evaluate_block()

            # Assignment Statement
            elif self.collection[self.curr_index][0].enum_type == WordType.IDENTIFIER:
                self.statements.append(Statement(self.collection[self.curr_index], StatementType.ASSIGNMENT))

            self.curr_index = self.curr_index + 1

    def print_block(self):
        print("<block> -> ", end='')
        for statement in self.statements:
            print("<" + statement.enum_type.string_type() + ">", end=' ')
        print("")
        for statement in self.statements:
            statement.print_statement()

    def find_end(self):
        find_end_index = self.curr_index + 1
        while find_end_index != self.end_index:
            if self.collection[find_end_index][0].enum_type == WordType.KEYWORD and self.collection[find_end_index][0].id == 7:
                return find_end_index
            else:
                find_end_index += 1
        raise Exception('Missing end for statement')
