# imports the Block class from block.py
from block import Block


class Blockchain:
    def __init__(self, chain=[], all_transactions=[]):
        self.chain = chain
        self.all_transactions = all_transactions
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        previous_hash = 0
        self.chain.append(Block(transactions, previous_hash))

    # add block to blockchain `chain`
    def add_block(self, transactions):
        transactions = transactions
        prev_hash = self.chain[len(self.chain) - 1].hash

        new_block = Block(transactions, prev_hash)

        self.chain.append(new_block)
