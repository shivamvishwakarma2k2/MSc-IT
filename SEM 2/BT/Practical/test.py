from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii

class Client:
    def __init__(self):
        # Generate RSA key pair
        self._private_key = RSA.generate(1024)
        self._public_key = self._private_key.publickey()

    @property
    def identity(self):
        # Return public key in hexadecimal format
        return binascii.hexlify(self._public_key.export_key(format='DER')).decode('ascii')

# Create a new client instance
client = Client()
print("Sender: ", client.identity)
