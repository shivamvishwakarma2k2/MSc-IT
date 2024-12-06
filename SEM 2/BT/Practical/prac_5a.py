import hashlib

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
    assert difficulty >= 1
    # Prefix of '1's based on difficulty
    prefix = '1' * difficulty
    print("Prefix:", prefix)
   
    for i in range(1000):
        # Create a hash using the message and the nonce (i)
        digest = sha256(str(hash(message)) + str(i))
        print("Testing --> " + digest)
       
        # Check if the hash starts with the desired prefix
        if digest.startswith(prefix):
            print("\nAfter", i, "iterations,\nfound nonce:", digest)
            return i  # Return the nonce value

# Run mining with difficulty level 2
mine("test message", 2)