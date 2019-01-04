# imports the Block class from block.py
from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    # add block to blockchain `chain`
    def add_block(self, transactions):
        prev_hash = self.chain[len(self.chain) - 1].hash

        new_block = Block(transactions, prev_hash)
        new_block.generate_hash()
        #proof = self.proof_of_work(new_block)
        # self.chain.append(new_block)
        self.chain.append(new_block)

    # print contents of blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block %s %s" % (i, current_block))
            current_block.print_block()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.generate_hash():
                print("Current hash does not equal generated hash")
                return False
            if previous.hash != previous.generate_hash():
                print("previous block hash dgot changed")
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != "0" * difficulty:
            block.nonce += 1
            proof = proof.generate_hash
        block.nonce = 0
        return proof
