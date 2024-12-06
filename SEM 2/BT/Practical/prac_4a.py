import binascii
import datetime
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from collections import OrderedDict

class Client:
    def __init__(self):
        random = Random.new().read
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
        return OrderedDict({
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

# Create clients
alice = Client()
bob = Client()
jhon = Client()

# Create transactions
transactions = []

t1 = Transaction(alice, bob.identity, 15.0)
t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(bob, jhon.identity, 25.0)
t2.sign_transaction()
transactions.append(t2)

t3 = Transaction(bob, jhon.identity, 200.0)
t3.sign_transaction()
transactions.append(t3)

# Display all transactions
tn = 1
for t in transactions:
    print("Transaction #", tn)
    display_transaction(t)
    tn += 1
    print()