from Scanner.Scanner import Scanner
from Parser.Parser import Parser
from Interpreter.Interpreter import Interpreter


def main():
    # Load in test code
    testcode = open("Test/testcode.txt", "r")
    contents = testcode.read()
    scan = Scanner()
    for symbol in contents:
        Scanner.read_symbol(scan, symbol)

    print("identifiers:")
    print(scan.identifiers)
    print("\n")
    print("consts:")
    print(scan.consts)
    print("________")

    for line in scan.lineCollection:
        for token in line:
            print("type: " + str(token.enum_type) + " id: " + str(token.id), end=' | ')
        print("")
    print("________")

    parser = Parser(Scanner.lineCollection)
    parsed_block = parser.parse()

    print("")
    print("________")
    print("")

    Interpreter.consts = scan.consts
    Interpreter.identifiers = scan.identifiers
    Interpreter.interpret(parsed_block.statements)


if __name__ == "__main__":
    main()
