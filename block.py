# import libraries
import datetime
from hashlib import sha256


class Block:
    # default constructor for block class
    def __init__(self, transactions, previous_hash, nonce=0):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.datetime.now()
        self.hash = self.generate_hash()  # cobines all the content within the block(digital figureprint)

    def print_block(self):
        # prints block contents
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())

    def generate_hash(self):
        # hash the blocks contents
        block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()
