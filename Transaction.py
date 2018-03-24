import SimpleCrypto as simplecrypto
class Transaction:
    def __init__(self, sender, recipient, amount, signature):
       self.sender = sender
       self.recipient = recipient
       self.amount = amount
       self.signature = signature


    def transaction_dump(self):
        return str(sefl.sender) + str(self.recipient) + str(self.amount)


    def sign_transaction(self, signature):
        self.signature = signature


    def is_valid(self):
        if()
