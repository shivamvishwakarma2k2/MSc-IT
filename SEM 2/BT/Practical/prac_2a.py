from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key():
    return get_random_bytes(8)


def encrypt(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = pad(message.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return ciphertext


def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = cipher.decrypt(ciphertext)
    unpadded_message = unpad(decrypted_message, DES.block_size)
    return unpadded_message.decode('utf-8')


if __name__ == "__main__":
    key = generate_key()
    message = "Hello, DES!"
    ciphertext = encrypt(message, key)
    print("Encrypted:", ciphertext.hex())
    decrypted_message = decrypt(ciphertext, key)
    print("Decrypted:", decrypted_message)
