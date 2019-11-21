class Collection:
    collection = []

    def __init__(self, set_collection):
        collection = set_collection

    @staticmethod
    def insert_collection(index, value):
        Collection.collection.insert(index, value)