from Scanner.WordType import WordType
from Parser.ExpressionType import ExpressionType
from Parser.OperatorType import OperatorType


class Expression:
    def __init__(self, enum_type, tokens):
        self.enum_type = enum_type
        self.tokens = tokens

        if enum_type == ExpressionType.ASSIGNMENT:
            if tokens[0].enum_type != WordType.IDENTIFIER or tokens[1].enum_type != WordType.OPERATOR or tokens[1].id != 0:
                raise Exception('Incorrect Assignment Statement')
            if len(self.tokens) == 3 and tokens[2].enum_type != WordType.IDENTIFIER and tokens[2].enum_type != WordType.NUMBER:
                raise Exception('Incorrect Assignment Statement')

        if enum_type == ExpressionType.ARITHMETIC:
            if (tokens[0].enum_type != WordType.IDENTIFIER and tokens[0].enum_type != WordType.NUMBER) or tokens[1].enum_type != WordType.OPERATOR or tokens[1].operator_type != OperatorType.ARITHMETIC:
                raise Exception('Incorrect Arithmetic Statement')

        if enum_type == ExpressionType.BOOLEAN:
            if (tokens[0].enum_type != WordType.IDENTIFIER and tokens[0].enum_type != WordType.NUMBER) or tokens[1].enum_type != WordType.OPERATOR or tokens[1].operator_type != OperatorType.RELATIVE:
                raise Exception('Incorrect Arithmetic Statement')

    def print_expression(self):
        if self.enum_type == ExpressionType.ASSIGNMENT:
            print("<assignment_expression> -> " + self.token_string())

        elif self.enum_type == ExpressionType.ARITHMETIC:
            print("<arithmetic_expression> -> " + self.token_string())

        elif self.enum_type == ExpressionType.BOOLEAN:
            print("<boolean_expression> -> " + self.token_string())

        for token in self.tokens:
            token.print_token()

    def token_string(self):
        if len(self.tokens) != 3 and self.enum_type == ExpressionType.ASSIGNMENT:
            return "<" + WordType.string_type(self.tokens[0].enum_type) + " id:" + str(self.tokens[0].id) + "> <" + WordType.string_type(self.tokens[1].enum_type) + " id:" + str(self.tokens[1].id) + "> <arithmetic_expression>"
        else:
            return "<" + WordType.string_type(self.tokens[0].enum_type) + " id:" + str(self.tokens[0].id) + "> <" + WordType.string_type(self.tokens[1].enum_type) + " id:" + str(self.tokens[1].id) + "> <" + WordType.string_type(self.tokens[2].enum_type) + " id:" + str(self.tokens[2].id) + ">"
