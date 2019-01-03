# The transaction are best represented as dictionary, with keys for the required fields and values specific to the transaction.

transaction1 = {
    'amount': '30',
    'sender': 'Alice',
    'reciever': 'Bob'
}

transaction2 = {
    'amount': '200',
    'sender': 'Bob',
    'reciever': 'Alice'
}

transaction3 = {
    'amount': '300',
    'sender': 'Alice',
    'reciever': 'Timothy'
}

# The transactions are all stored inside the mempool
# A pool of transactions that miners reference when selecting the set of transactions they want to verify.

mempool = [transaction1, transaction2, transaction3]

block_transactions = [transaction1, transaction2, transaction3]
