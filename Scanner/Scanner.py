import re
from Scanner.WordType import WordType
from Scanner.SymbolType import SymbolType
from Scanner.Token import Token


class Scanner:
    output = open("testoutput.txt", "w+")

    lowercase_pattern = '[a-z]'
    number_pattern = '[0-9]'

    identifiers = []
    consts = []
    currentTokenLine = []
    lineCollection = []
    operators = ['=', '>=', '<=', '<', '>', '==', '!=', '~=', '+', '-', '*', '/']
    keywords = ['if', 'while', 'print', 'function', 'repeat', 'for', 'else', 'end']
    symbols = ['(', ')', '.', ':']

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

        elif symbol == "(" or symbol == ")" or symbol == "." or symbol == ":":
            self.last_token = SymbolType.SYMBOL
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
        self.lineCollection.append(self.currentTokenLine)
        self.currentTokenLine = []
        self.output.write("\n")

    def add_keyword(self):
        self.word_keyword_validity_check()
        self.last_word = WordType.KEYWORD
        self.currentTokenLine.append(Token(WordType.KEYWORD, self.keywords.index(self.current_token_string), self.current_token_string))
        self.output.write("<KeywordId " + "Lexeme:" + self.current_token_string + " Token:" +
                          str(self.keywords.index(self.current_token_string)) + "> ")

    def add_operator(self):
        self.word_operator_validity_check()
        self.last_word = WordType.OPERATOR
        self.currentTokenLine.append(Token(WordType.OPERATOR, self.operators.index(self.current_token_string), self.current_token_string))
        self.output.write("<OperatorId " + "Lexeme:" + self.current_token_string + " Token:" +
                          str(self.operators.index(self.current_token_string)) + "> ")

    def add_symbol(self):
        self.word_symbol_validity_check()
        self.last_word = WordType.SYMBOL
        self.currentTokenLine.append(Token(WordType.SYMBOL, self.symbols.index(self.current_token_string), self.current_token_string))
        self.output.write("<SymbolId " + "Lexeme:" + self.current_token_string + " Token:" +
                          str(self.symbols.index(self.current_token_string)) + "> ")

    def add_const(self):
        self.word_number_validity_check()
        self.last_word = WordType.NUMBER
        if self.current_token_string not in self.consts:
            self.consts.append(self.current_token_string)
            self.output.write("<ConstId " + "Lexeme:" + self.current_token_string + " Token:" +
                              str(len(self.consts) - 1) + "> ")
            self.currentTokenLine.append(Token(WordType.NUMBER, len(self.consts) - 1, self.current_token_string))

        else:
            self.output.write("<ConstId " + "Lexeme:" + self.current_token_string + " Token:" +
                              str(self.consts.index(self.current_token_string)) + "> ")
            self.currentTokenLine.append(Token(WordType.NUMBER, self.consts.index(self.current_token_string), self.current_token_string))

    def add_identifier(self):
        self.word_identifier_validity_check()
        self.last_word = WordType.IDENTIFIER
        if self.current_token_string not in self.identifiers:
            self.identifiers.append(self.current_token_string)
            self.output.write("<IdentifierId " + "Lexeme:" + self.current_token_string + " Token:" +
                              str(len(self.identifiers) - 1) + "> ")
            self.currentTokenLine.append(Token(WordType.IDENTIFIER, len(self.identifiers) - 1, self.current_token_string))

        else:
            self.output.write("<IdentifierId " + "Lexeme:" + self.current_token_string + " Token:" +
                              str(self.identifiers.index(self.current_token_string)) + "> ")
            self.currentTokenLine.append(Token(WordType.IDENTIFIER, self.identifiers.index(self.current_token_string), self.current_token_string))

    def keyword_substring_check(self):
        check = False
        for string in self.keywords:
            if self.current_token_string in string:
                check = True

        if not check:
            raise Exception(
                'Invalid token at line {}, index {}'.format(str(self.current_line), str(self.current_line_index)))

    def symbol_substring_check(self, symbol):
        check = False
        self.current_token_string += symbol
        for string in self.symbols:
            if self.current_token_string in string:
                check = True

        return check

    def operator_substring_check(self, symbol):
        check = False
        self.current_token_string += symbol
        for string in self.operators:
            if self.current_token_string in string:
                check = True

        return check

    def word_operator_validity_check(self):
        if self.last_word == WordType.OPERATOR:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def word_number_validity_check(self):
        if self.last_word == WordType.NUMBER or self.last_word == WordType.IDENTIFIER:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def word_keyword_validity_check(self):
        if self.last_word == WordType.KEYWORD or self.last_word == WordType.NUMBER or \
                self.last_word == WordType.IDENTIFIER or self.last_word == WordType.OPERATOR:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def word_identifier_validity_check(self):
        if self.last_word == WordType.IDENTIFIER or self.last_word == WordType.NUMBER:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def word_symbol_validity_check(self):
        if self.last_word != WordType.KEYWORD and self.last_word != WordType.IDENTIFIER and \
                self.last_word != WordType.NUMBER and self.last_word != WordType.SYMBOL:
            raise Exception('Invalid word at line {}'.format(str(self.current_line)))

    def letter_validity_check(self):
        if self.last_token == SymbolType.LETTER:
            self.keyword_substring_check()

        elif self.last_token != SymbolType.SPACE and self.last_token != SymbolType.NEWLINE:
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

