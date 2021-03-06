import SimpleCrypto as simplecrypto
class Transaction:
    def __init__(self, sender, recipient, amount, signature):
       self.sender = sender
       self.recipient = recipient
       self.amount = amount
       self.signature = signature


    def dump(self):
        return str(self.sender) + str(self.recipient) + str(self.amount)


    def sign_transaction(self, signature):
        self.signature = signature


    def is_valid(self):
        if simplecrypto.decrypt(self.sender, self.signature) == self.dump():
            return True
        else:
            return False
