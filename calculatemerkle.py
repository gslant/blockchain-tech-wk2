import pandas as pd
import hashlib as hash

def calculate_root(transactions):
    if len(transactions) == 0:
        return None

    def hash_pair(hash1, hash2):
        combined = hash1 + hash2
        return hash.sha256(combined.encode()).hexdigest()
    
    hashes = list(transactions['hash'])

    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])

        new_hashes = []
        for i in range(0, len(hashes), 2):
            new_hashes.append(hash_pair(hashes[i], hashes[i+1]))

        hashes = new_hashes

    return hashes[0]

df = pd.read_csv('bitcoin_block_641818.csv')
merkle_root = calculate_root(df)
print(merkle_root)
