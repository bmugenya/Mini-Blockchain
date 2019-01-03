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

    # print contents of blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block %s %s" % (i, current_block))

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.generate_hash():
                return False
            if previous.hash != previous.generate_hash():
                return False
        return True
