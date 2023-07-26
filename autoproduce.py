import hashlib as hash
import pickle
import time

class Block:
    def __init__(self, height, prev_hash, timestamp, merkle_root, transactions):
        self.height = height
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.merkle_root = merkle_root
        self.transactions = transactions

    def calculate_hash(self):
        byte_self = pickle.dumps(self)
        return hash.sha1(byte_self).hexdigest()
    
def create_genesis_block():   
    return Block(1, 'this is the genesis block', time.time(), '', [])

def create_new_block(prev_block, transactions):
    new_block_height = prev_block.height + 1
    new_block_timestamp = time.time()
    return Block(new_block_height, prev_block.calculate_hash(), new_block_timestamp, '', transactions)

def mine_block(prev_block, transactions, block_time):
    new_block = create_new_block(prev_block, transactions)
    print(f"Mining Block {new_block.height}...")
    time.sleep(block_time)
    return new_block

def generate_random_transactions():
    transactions = []
    for i in range(1, 6):
        transaction = f"Transaction {i}"
        transactions.append(transaction)
    return transactions

def main():
    block_time = 5

    gen_block = create_genesis_block()

    prev_block = gen_block

    while True:
        new_block = mine_block(prev_block, generate_random_transactions, block_time)
        print(f"Block mined at {new_block.timestamp}.")
        prev_block = new_block

if __name__ == "__main__":
    main()