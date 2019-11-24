from Parser.StatementType import StatementType
from Parser.ExpressionType import ExpressionType
from Parser.ParsingObjects.Expression import Expression
from Scanner.WordType import WordType
from Scanner.Token import Token
from Scanner.Scanner import Scanner
from Parser.ParsingObjects.Collection import Collection

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

    current_line = 0

    def __init__(self, line, enum_type):
        self.blocks = []
        self.expressions = []
        self.print_token = []
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

        elif enum_type == StatementType.PRINT:
            if len(line) == 4:
                self.print_token.append(line[2])
            else:
                self.expressions.append(Expression(ExpressionType.ARITHMETIC, line[2:5]))

        elif enum_type == StatementType.FOR:
            self.build_for(line)

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
            self.blocks[0].print_block()

        elif self.enum_type == StatementType.CONDITIONAL:
            print("<conditional_statement> -> if <boolean_expression> then <block> else <block>")
            self.expressions[0].print_expression()
            self.blocks[0].print_block()

        elif self.enum_type == StatementType.PRINT:
            if len(self.print_token) != 0:
                print("<print_statement> -> print ( <" + self.print_token[0].enum_type.string_type() + "> )")
                self.print_token[0].print_token()
            else:
                print("<print_statement> -> print ( <arithmetic_expression> )")
                self.expressions[0].print_expression()

        elif self.enum_type == StatementType.FOR:
            print("<for_statement> -> <assignment_statement> <while_statement> <assignment_statement>")

        elif self.enum_type == StatementType.ELSE:
            self.blocks[0].print_block()

    def build_for(self, line):
        assignment_line = []
        while_line = []
        increment_line = []

        increment_from_identifier = str(line[1].value)
        increment_from_value = str(int(line[3].value) - 1)
        increment_to = str(int(line[5].value))

        if increment_from_identifier not in Scanner.identifiers:
            Scanner.identifiers.append(increment_from_identifier)
            identifer_id = len(Scanner.identifiers) - 1
        else:
            identifer_id = Scanner.identifiers.index(increment_from_identifier)

        if increment_from_value not in Scanner.consts:
            Scanner.consts.append(increment_from_value)
            from_id = len(Scanner.consts) - 1
        else:
            from_id = Scanner.consts.index(increment_from_value)

        if increment_to not in Scanner.consts:
            Scanner.consts.append(increment_to)
            to_id = len(Scanner.consts) - 1
        else:
            to_id = Scanner.consts.index(increment_to)

        if 1 not in Scanner.consts:
            Scanner.consts.append(1)
            one_id = len(Scanner.consts) - 1
        else:
            one_id = Scanner.consts.index(1)

        loop_identifier_token = Token(WordType.IDENTIFIER, identifer_id, increment_from_identifier)
        loop_operator_token = Token(WordType.OPERATOR, 0, '=')
        loop_assignment_integer = Token(WordType.NUMBER, from_id, increment_from_value)

        assignment_line.append(loop_identifier_token)
        assignment_line.append(loop_operator_token)
        assignment_line.append(loop_assignment_integer)

        loop_while = Token(WordType.KEYWORD, 1, 'while')
        loop_less_than = Token(WordType.OPERATOR, 3, '<')
        loop_lt_integer = Token(WordType.NUMBER, to_id, increment_to)

        while_line.append(loop_while)
        while_line.append(loop_identifier_token)
        while_line.append(loop_less_than)
        while_line.append(loop_lt_integer)

        increment_add = Token(WordType.OPERATOR, 8, '+')
        one_add = Token(WordType.NUMBER, one_id, "1")

        increment_line.append(loop_identifier_token)
        increment_line.append(loop_operator_token)
        increment_line.append(loop_identifier_token)
        increment_line.append(increment_add)
        increment_line.append(one_add)

        Collection.insert_collection(Statement.current_line + 2, assignment_line)
        Collection.insert_collection(Statement.current_line + 3, while_line)
        Collection.insert_collection(Statement.current_line + 4, increment_line)
