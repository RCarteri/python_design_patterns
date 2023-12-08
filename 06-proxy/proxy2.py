from abc import ABCMeta, abstractmethod

#Interface
class Wallet(metaclass=ABCMeta):
    @abstractmethod
    def pay(self):
        pass

#Real Object
class BankWallet(Wallet):
    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __has_balance(self):
        print("Bank Wallet: Checking if account has enough balance")
        return True

    def set_card(self, card):
        self.card = card

    def pay(self):
        if self.__has_balance():
            print("Bank Wallet: Paying the merchant")
            return True
        else:
            print("Bank Wallet: Sorry, not enough funds")
            return False

#Proxy
class DebitCardWallet(Wallet):
    def __init__(self):
        self.bank_wallet = BankWallet()

    def pay(self):
        card = input("Proxy: Punch in card number: ")
        self.bank_wallet.set_card(card)
        return self.bank_wallet.pay()


#Client
class Customer:
    def __init__(self):
        print("Customer: I'd like to pay using my debit card")
        self.wallet = DebitCardWallet()
        self.wallet.pay()

    def __del__(self):
        print("Customer: Thank you for your service")

Customer()