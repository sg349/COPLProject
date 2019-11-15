from Parser.StatementType import StatementType
from Parser.ExpressionType import ExpressionType
from Parser.ParsingObjects.Expression import Expression


class Statement:
    expressions = []

    def __init__(self, line, type):
        self.line = line
        self.type = type

        if type == StatementType.ASSIGNMENT:
            if len(line) == 3:
                expression = Expression(ExpressionType.ASSIGNMENT, line)

    def print_statement(self):

            expression.print_expression()