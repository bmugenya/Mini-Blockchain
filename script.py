from blockchain import Blockchain
from hashlib import sha256

new_transactions = [{'amount': '30', 'sender': 'alice', 'receiver': 'bob'},
                    {'amount': '55', 'sender': 'bob', 'receiver': 'alice'}]

my_blockchain = Blockchain()

my_blockchain.add_block(new_transactions)

print(my_blockchain.print_blocks)


# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof
proof = str(nonce) + str(new_transactions)
proof = sha256(proof.encode()).hexdigest()
# printing proof
print(proof)


# finding a proof that has 2 leading zeros
while proof[:2] != "0" * difficulty:
    nonce += 1
    proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()

# printing final proof that was found
final_proof = proof
print(final_proof)
