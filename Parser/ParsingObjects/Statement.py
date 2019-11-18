from Parser.StatementType import StatementType
from Parser.ExpressionType import ExpressionType
from Parser.ParsingObjects.Expression import Expression

# Coogan Koerts, Brent Einolf, Sam Gardiner

# This file contains all of the information to determine if the statement passed to this class is either a Arithmetic,
# Conditional, Assignment, While, Repeat, For or a Print statement. From there some of the statements can be broken down
# into expressions. This class is also contains the print functions for statements.

ARITHMETIC = 1
CONDITIONAL = 2
ASSIGNMENT = 3
WHILE = 4
REPEAT = 5
FOR = 6
PRINT = 7

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
        elif enum_type == StatementType.WHILE:
            self.expressions.append(Expression(ExpressionType.BOOLEAN, line[1:4]))
        elif enum_type == StatementType.CONDITIONAL:
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

        elif self.enum_type == StatementType.WHILE:
            print("<while_statement> -> while <boolean_expression> then <block>")
            self.expressions[0].print_expression()

        elif self.enum_type == StatementType.CONDITIONAL:
            print("<conditional_statement> -> if <boolean_expression> then <block> else <block>")
            self.expressions[0].print_expression()

        elif self.enum_type == StatementType.PRINT:
            print("<print_statement> -> print ( <block> )")
