import re
from Scanner.SymbolType import SymbolType
from Scanner.SymbolType import WordType


class Scanner:
    output = open("testoutput.txt", "w+")

    lowercase_pattern = '[a-z]'
    number_pattern = '[0-9]'

    identifiers = []
    consts = []
    operators = ['=', '>=', '<=', '<', '>', '==', '~=', '+', '-', '*', '/']
    keywords = ['if', 'while', 'print', 'function', 'repeat']

    last_word = None
    last_token = SymbolType.NEWLINE
    current_token_string = ''
    current_global_index = 0
    current_line_index = 0
    current_line = 1

    def read_symbol(self, symbol):
        if symbol == " ":
            self.space_validity_check()
            self.add_token()
            self.last_token = SymbolType.SPACE
            self.current_line_index += 1
            self.current_global_index += 1

        elif symbol == "(":
            if self.last_token != SymbolType.LETTER:
                raise Exception(
                    'Invalid token at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))
            self.add_token()
            self.last_token = SymbolType.SYMBOL
            self.current_line_index += 1
            self.current_global_index += 1

        elif symbol == ")":
            if self.last_token != "(" and self.last_token != SymbolType.LETTER:
                raise Exception(
                    'Invalid token at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))
            self.add_token()
            self.last_token = SymbolType.SYMBOL

        elif symbol == ".":
            if self.last_token != SymbolType.LETTER:
                raise Exception(
                    'Invalid token at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))
            self.add_token()
            self.last_token = SymbolType.SYMBOL

        elif symbol == "\n":
            self.newline_validity_check()
            self.add_token()
            self.add_newline()
            self.last_token = SymbolType.NEWLINE
            self.current_line_index = 0
            self.current_line += 1
            self.current_global_index += 1

        elif re.search(self.lowercase_pattern, symbol):
            self.current_token_string += symbol
            self.letter_validity_check()
            self.last_token = SymbolType.LETTER
            self.current_line_index += 1
            self.current_global_index += 1

        elif re.search(self.number_pattern, symbol):
            self.current_token_string += symbol
            self.number_validity_check()
            self.last_token = SymbolType.NUMBER
            self.current_line_index += 1
            self.current_global_index += 1

        elif self.operator_substring_check(symbol):
            self.last_token = SymbolType.OPERATOR
            self.current_line_index += 1
            self.current_global_index += 1

        else:
            raise Exception(
                'Invalid token at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))

    def add_token(self):
        if self.last_token == SymbolType.LETTER:

            if len(self.current_token_string) > 1:
                self.keyword_substring_check()
                self.add_keyword()

            elif len(self.current_token_string) == 1:
                self.add_identifier()

        elif self.last_token == SymbolType.NUMBER:
            self.add_const()

        elif self.last_token == SymbolType.OPERATOR:
            self.add_operator()

        elif self.last_token == SymbolType.SYMBOL:
            self.add_symbol()

        self.current_token_string = ''

    def add_newline(self):
        self.last_word = WordType.NEWLINE
        self.output.write("\n")

    def add_keyword(self):
        self.word_keyword_validity_check()
        self.last_word = WordType.KEYWORD
        self.output.write("<KeywordId " + str(self.keywords.index(self.current_token_string)) + "> ")

    def add_operator(self):
        self.word_operator_validity_check()
        self.last_word = WordType.OPERATOR
        self.output.write("<OperatorId " + str(self.operators.index(self.current_token_string)) + "> ")

    def add_const(self):
        self.word_number_validity_check()
        self.last_word = WordType.NUMBER
        if self.current_token_string not in self.identifiers:
            self.consts.append(self.current_token_string)
            self.output.write("<ConstId " + str(len(self.consts) - 1) + "> ")

        else:
            self.output.write("<ConstId " + str(self.consts.index(self.current_token_string)) + "> ")

    def add_identifier(self):
        self.word_identifier_validity_check()
        self.last_word = WordType.IDENTIFIER
        if self.current_token_string not in self.identifiers:
            self.identifiers.append(self.current_token_string)
            self.output.write("<IdentifierId " + str(len(self.identifiers) - 1) + "> ")

        else:
            self.output.write("<IdentifierId " + str(self.identifiers.index(self.current_token_string)) + "> ")

    def add_symbol(self):
        self.word_symbol_validity_check()

    def word_operator_validity_check(self):
        if self.last_word == WordType.OPERATOR:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def word_number_validity_check(self):
        if self.last_word == WordType.NUMBER or self.last_word == WordType.IDENTIFIER:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def word_keyword_validity_check(self):
        if self.last_word == WordType.KEYWORD or self.last_word == WordType.NUMBER or self.last_word == WordType.IDENTIFIER or self.last_word == WordType.OPERATOR:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def word_identifier_validity_check(self):
        if self.last_word == WordType.IDENTIFIER or self.last_word == WordType.NUMBER:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def word_symbol_validity_check(self):
        if self.last_word != WordType.KEYWORD and self.last_word != WordType.IDENTIFIER:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def keyword_substring_check(self):
        check = False
        for string in self.keywords:
            if self.current_token_string in string:
                check = True

        if not check:
            raise Exception(
                'Invalid token at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))

    def operator_substring_check(self, symbol):
        check = False
        self.current_token_string += symbol
        for string in self.operators:
            if self.current_token_string in string:
                check = True

        return check

    def letter_validity_check(self):
        if self.last_token == SymbolType.LETTER:
            self.keyword_substring_check()

        elif self.last_token != SymbolType.SPACE and self.last_token != SymbolType.NEWLINE and self.last_token != SymbolType.SYMBOL:
            raise Exception(
                'Invalid token at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))

    def number_validity_check(self):
        if self.last_token == SymbolType.LETTER and self.last_token == SymbolType.OPERATOR:
            raise Exception(
                'Invalid token at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))

        if abs(float(self.current_token_string)) > 0xffffffff:
            raise Exception(
                'Number too large at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))

    def space_validity_check(self):
        if self.last_token == SymbolType.NEWLINE:
            raise Exception('Unexpected Space at start of line {}'.format(self.current_line))

        if self.last_token == SymbolType.SPACE:
            raise Exception(
                'Double Space at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))

    def newline_validity_check(self):
        if self.last_token == SymbolType.OPERATOR:
            raise Exception('Unexpected end of line at line {}'.format(str(self.current_line)))



