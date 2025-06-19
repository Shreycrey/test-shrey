from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def get_random_number(): 
    global seed
    seed = int(str(seed * seed).zfill(12)[3:9]) 
    return seed

# Replace this with the ciphertext you got from encrypting "message"
target_ciphertext = bytes.fromhex('89f08e12023250ef8ebaa134e64e5a15')
known_plaintext = b'message'

for possible_seed in range(10**6):
    print(f"Trying seed: {possible_seed}", end='\r')
    seed = possible_seed
    key = b''
    for _ in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = unpad(cipher.decrypt(target_ciphertext), AES.block_size)
    except:
        continue
    if decrypted == known_plaintext:
        print("Found seed:", possible_seed)
        print("Key to submit:", key.hex())
        break

