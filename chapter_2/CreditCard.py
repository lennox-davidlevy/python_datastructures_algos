class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._limit = limit
        self._acnt = acnt
        self._bank = bank
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_limit(self):
        return self._limit

    def get_account(self):
        return self._acnt

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if (self._balance + price) <= self._limit:
            self._balance += price
            if self._close_to_limit():
                print(f"Available credit at {self.get_available_credit()}%")
            return True
        else:
            print(f"Cannot charge! Available credit at {self.get_available_credit()}%")
            return False

    def make_payment(self, payment):
        if payment > self._balance:
            delta = payment - self._balance
            self._balance = 0
            return self._balance
        else:
            self._balance -= payment
            return self._balance

    def get_available_credit(self):
        usage = (self._balance / self._limit) * 100
        return 100 - usage

    def _close_to_limit(self):
        return self.get_available_credit() <= 10

    def __str__(self):
        return f"{str(self.__class__)}: {str(self.__dict__)}"


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("David Levy", "Capital One", "1234-5678-9012", 2500))
    wallet.append(CreditCard("David Levy", "TD", "1234-5678-9012", 3500))
    wallet.append(CreditCard("David Levy", "Chase", "1234-5678-9012", 4500))
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print(f"Customer = {wallet[c].get_customer()}")
        print(f"Bank = {wallet[c].get_bank()}")
        print(f"Account = {wallet[c].get_account()}")
        print(f"Limit = {wallet[c].get_limit()}")
        print(f"Balance = {wallet[c].get_balance()}")
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f"New Balance = {wallet[c].get_balance()}")
