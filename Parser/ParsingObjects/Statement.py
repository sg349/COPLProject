from Parser.StatementType import StatementType
from Parser.ExpressionType import ExpressionType
from Parser.ParsingObjects.Expression import Expression


class Statement:

    def __init__(self, line, enum_type):
        self.expressions = []
        self.line = line
        self.enum_type = enum_type

        if enum_type == StatementType.ASSIGNMENT:
            if len(line) == 3:
                self.expressions.append(Expression(ExpressionType.ASSIGNMENT, line))
            else:
                self.expressions.append(Expression(ExpressionType.ASSIGNMENT, line[0:2]))
                self.expressions.append(Expression(ExpressionType.ARITHMETIC, line[2:5]))
        if enum_type == StatementType.WHILE:
            self.expressions.append(Expression(ExpressionType.BOOLEAN, line[1:4]))

    def print_statement(self):
        if self.enum_type == StatementType.ASSIGNMENT:
            if len(self.line) == 3:
                print("<assignment_statement> -> <assignment_expression>")
                self.expressions[0].print_expression()
            else:
                print("<assignment_statement> -> <assignment_expression> <arithmetic_expression>")
                for expression in self.expressions:
                    expression.print_expression()

        if self.enum_type == StatementType.WHILE:
            print("<while_statement> -> while <boolean_expression> then <block>")
            self.expressions[0].print_expression()
