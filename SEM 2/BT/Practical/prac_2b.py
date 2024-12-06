import datetime
import hashlib

def sha256(message):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()
   
    # Update the hash object with the bytes-like object (message)
    sha256_hash.update(message.encode('utf-8'))
   
    # Get the hexadecimal representation of the digest
    digest = sha256_hash.hexdigest()
   
    return digest

print(datetime.datetime.now())
message = "6620_Shivam"
result = sha256(message)
print(f"SHA-256 Digest for '{message}': {result}")