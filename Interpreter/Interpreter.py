from Parser.StatementType import StatementType
from Scanner.WordType import WordType
from Scanner.Token import Token


class Interpreter:

    key_value_pair = {}
    identifiers = []
    consts = []

    @staticmethod
    def interpret(statements):
        else_flag = False
        for statement in statements:
            if statement.enum_type == StatementType.PRINT:
                if len(statement.expressions) == 0:
                    Interpreter.print_token(statement.line[2])
                else:
                    Interpreter.print_token(Interpreter.interpret_arithmetic(statement.expressions[0].tokens))

            elif statement.enum_type == StatementType.ASSIGNMENT:
                if len(statement.expressions) == 1:
                    Interpreter.interpret_assignment(statement.expressions[0].tokens)
                else:
                    line = [statement.line[0], statement.line[1], Interpreter.interpret_arithmetic(statement.line[2:5])]
                    Interpreter.interpret_assignment(line)

            elif statement.enum_type == StatementType.CONDITIONAL:
                if Interpreter.interpret_boolean(statement.expressions[0].tokens):
                    Interpreter.interpret(statement.blocks[0].statements)
                else:
                    else_flag = True

            elif statement.enum_type == StatementType.ELSE and else_flag:
                Interpreter.interpret(statement.blocks[0].statements)
                else_flag = False

            elif statement.enum_type == StatementType.WHILE:
                while Interpreter.interpret_boolean(statement.expressions[0].tokens):
                    Interpreter.interpret(statement.blocks[0].statements)

    @staticmethod
    def interpret_assignment(tokens):
        if tokens[2].enum_type == WordType.NUMBER:
            Interpreter.key_value_pair[Interpreter.identifiers[tokens[0].id]] = Interpreter.consts[tokens[2].id]

        if tokens[2].enum_type == WordType.IDENTIFIER:
            Interpreter.key_value_pair[Interpreter.identifiers[tokens[0].id]] = Interpreter.key_value_pair[Interpreter.identifiers[tokens[2].id]]

    @staticmethod
    def interpret_arithmetic(tokens):
        arithmetic_string = ''
        if tokens[0].enum_type == WordType.IDENTIFIER:
            arithmetic_string += str(Interpreter.key_value_pair[Interpreter.identifiers[tokens[0].id]])
        else:
            arithmetic_string += str(Interpreter.consts[tokens[0].id])

        arithmetic_string += tokens[1].value

        if tokens[2].enum_type == WordType.IDENTIFIER:
            arithmetic_string += str(Interpreter.key_value_pair[Interpreter.identifiers[tokens[2].id]])
        else:
            arithmetic_string += str(Interpreter.consts[tokens[2].id])

        number = str(eval(arithmetic_string))

        if number not in Interpreter.consts:
            Interpreter.consts.append(number)
            num_id = len(Interpreter.consts) - 1
        else:
            num_id = Interpreter.consts.index(number)

        return Token(WordType.NUMBER, num_id, number)

    @staticmethod
    def interpret_boolean(tokens):
        bool_string = ''
        if tokens[0].enum_type == WordType.IDENTIFIER:
            bool_string += str(Interpreter.key_value_pair[Interpreter.identifiers[tokens[0].id]])
        else:
            bool_string += str(Interpreter.consts[tokens[0].id])

        bool_string += tokens[1].value

        if tokens[2].enum_type == WordType.IDENTIFIER:
            bool_string += str(Interpreter.key_value_pair[Interpreter.identifiers[tokens[2].id]])
        else:
            bool_string += str(Interpreter.consts[tokens[2].id])

        return eval(bool_string)

    @staticmethod
    def print_token(token):
        if token.enum_type == WordType.NUMBER:
            print(Interpreter.consts[token.id])

        if token.enum_type == WordType.IDENTIFIER:
            print(Interpreter.key_value_pair[Interpreter.identifiers[token.id]])
