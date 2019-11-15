from Scanner.WordType import WordType
from Parser.ExpressionType import ExpressionType


class Expression:
    def __init__(self, type, tokens):
        self.type = type
        self.tokens = tokens

        if type == ExpressionType.ASSIGNMENT:
            if tokens[0].type != WordType.IDENTIFIER or tokens[1].type != WordType.OPERATOR or tokens[1].id != 1:
                raise Exception('Incorrext Assignment Statement')

    def print_expression(self):
        if type == ExpressionType.ASSIGNMENT:
            print(len("<assignment_expression> -> " + self.token_string()))

    def token_string(self):
        return "<" + self.tokens[0].type.string_type() + " id:" + str(self.tokens[0].id()) + "> " + "<" + self.tokens[1].type.string_type() + " id:" + str(self.tokens[1].id()) + ">" + self.tokens[2].type.string_type() + " id:" + str(self.tokens[2].id()) + ">"