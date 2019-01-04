# import libraries
import datetime
from hashlib import sha256


class Block:
    # default constructor for block class
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = datetime.datetime.now()
        self.hash = self.generate_hash()  # cobines all the content within the block(digital figureprint)

    def print_block(self):
        # prints block contents
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)
        print("\n")

    def generate_hash(self):
        # hash the blocks contents
        block_contents = str(self.time_stamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()
