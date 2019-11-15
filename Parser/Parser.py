from Scanner.WordType import WordType
from Parser.ParsingObjects.Block import Block


class Parser:
    def __init__(self, lineCollection):
        self.lineCollection = lineCollection

    def parse(self):
        collection_size = len(self.lineCollection)
        if self.lineCollection[0][0].type != WordType.KEYWORD or self.lineCollection[0][0].id != 3:
            raise Exception("Expected Function at start of file")
        if self.lineCollection[collection_size - 1][0].type != WordType.KEYWORD or self.lineCollection[collection_size - 1][0].id != 7 or len(self.lineCollection[collection_size - 1]) != 1:
            raise Exception("Expected End at End of file")

        start_block = Block(1, collection_size - 1, self.lineCollection)
        start_block.evaluate_block()
