from Scanner.WordType import WordType
from Parser.ParsingObjects.Statement import Statement
from Parser.StatementType import StatementType
from Parser.ParsingObjects.Collection import Collection

# Coogan Koerts, Brent Einolf, Sam Gardiner

# This class is used as starting point for each "block" statement. From here the "block" will be broken broken down by
# each statement with in and from there each statement will be determined what type of statement it is and whether or
# not it is an expression. This class is also contains the print functions for the block statements.


class Block:
    current_index = 1

    def __init__(self, collection):
        self.start_index = Block.current_index
        Collection.collection = collection
        self.collection = collection
        self.statements = []

    def evaluate_block(self):
        while True:
            c = Collection.collection
            print("")
            if len(Collection.collection) <= Block.current_index:
                break

            if Collection.collection[Block.current_index][0].enum_type == WordType.KEYWORD and Collection.collection[Block.current_index][0].id == 7:
                Block.current_index += 1
                break

            # Keyword Statement
            if Collection.collection[Block.current_index][0].enum_type == WordType.KEYWORD:
                # conditional statement
                if Collection.collection[Block.current_index][0].id == 0:
                    statement = Statement(Collection.collection[Block.current_index], StatementType.CONDITIONAL)
                    self.statements.append(statement)
                    Block.current_index += 1
                    statement_block = Block(Collection.collection)
                    statement_block.evaluate_block()
                    statement.blocks.append(statement_block)

                # else statement
                elif Collection.collection[Block.current_index][0].id == 6:
                    statement = Statement(Collection.collection[Block.current_index], StatementType.ELSE)
                    self.statements.append(statement)
                    Block.current_index += 1
                    statement_block = Block(Collection.collection)
                    statement_block.evaluate_block()
                    statement.blocks.append(statement_block)


                # while statement
                elif Collection.collection[Block.current_index][0].id == 1:
                    statement = Statement(Collection.collection[Block.current_index], StatementType.WHILE)
                    self.statements.append(statement)
                    Block.current_index += 1
                    statement_block = Block(Collection.collection)
                    statement_block.evaluate_block()
                    statement.blocks.append(statement_block)

                # print statement
                elif Collection.collection[Block.current_index][0].id == 2:
                    self.statements.append(Statement(Collection.collection[Block.current_index], StatementType.PRINT))
                    Block.current_index += 1

                # for statement
                elif Collection.collection[Block.current_index][0].id == 5:
                    self.statements.append(Statement(Collection.collection[Block.current_index], StatementType.FOR))
                    Block.current_index += 1

            # Assignment Statement
            elif Collection.collection[Block.current_index][0].enum_type == WordType.IDENTIFIER:
                self.statements.append(Statement(Collection.collection[Block.current_index], StatementType.ASSIGNMENT))
                Block.current_index += 1

        Statement.current_line = Block.current_index

    def print_block(self):
        print("<block> -> ", end='')
        for statement in self.statements:
            print("<" + statement.enum_type.string_type() + ">", end=' ')
        print("")
        for statement in self.statements:
            statement.print_statement()
