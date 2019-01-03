# import datetime library
import datetime


class Block:
    # default constructor for block class
    def __init__(self, transactions, previous_hash, nonce=0):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.datetime.now()
