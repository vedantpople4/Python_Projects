from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("Mined Bitcoin with nonce value: ", {nonce})
            return new_hash

    raise BaseException("Couldnt find correct has after trying {MAX_NONCE} times")

if __name__ =='__main__':
    transactions= A->B->20,
    F->G->40 
    difficulty = 4

    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5, transactions, '6b88c087247aa2f07ee1c5956b8e1a9f4c7f892a70e324f1bb3d161e05ca107b', difficulty)
    total_time = str((time.time() - start()))
    print("End Mining, Mining took: {total_time} seconds")
    print(new_hash)
