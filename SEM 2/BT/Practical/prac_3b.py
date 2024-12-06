import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import binascii
import datetime
import collections

class Client:
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf-8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

def display_transaction(transaction):
    _dict = transaction.to_dict()
    print("sender: " + _dict['sender'])
    print()
    print("recipient: " + _dict['recipient'])
    print()
    print("value: " + str(_dict['value']))
    print()
    print("time: " + str(_dict['time']))
    print()

# Create two clients and a transaction between them
transactions = []
A = Client()
B = Client()

# Create a transaction from A to B
t1 = Transaction(A, B.identity, 15.0)

# Sign the transaction
signature = t1.sign_transaction()

# Display the transaction
display_transaction(t1)
print("Signature:", signature)