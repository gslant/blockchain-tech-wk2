import pandas as pd
import hashlib
import codecs

def calculate_merkle_root(transactions):

    # Convert transaction hashes to a list and reverse each hash (little-endian to big-endian)
    hashes = [codecs.decode(tx_hash, 'hex')[::-1] for tx_hash in transactions['hash']]

    while len(hashes) > 1:
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])  # Duplicate last hash if odd number

        new_hashes = []
        for i in range(0, len(hashes), 2):
            combined_hash = hashes[i] + hashes[i+1]
            new_hashes.append(hashlib.sha256(hashlib.sha256(combined_hash).digest()).digest())

        hashes = new_hashes

    # Reverse the final hash to get the merkle root in big-endian order
    merkle_root = hashes[0][::-1].hex()
    return merkle_root

def main():
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('bitcoin_block_641818.csv')

    # Calculate the Merkle root
    merkle_root = calculate_merkle_root(df)

    # Print the Merkle root
    print("Merkle Root:", merkle_root)

    if(merkle_root == 'eaff941d295642c5176c4464b6d7b6f43ef3257c9ff5b8570bca59fd18c31af8'):
        print("Merkle Root is correct")

if __name__ == "__main__":
    main()