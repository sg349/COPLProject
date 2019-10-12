from Scanner.Scanner import Scanner


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


if __name__ == "__main__":
    main()
