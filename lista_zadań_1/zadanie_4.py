class Account:
    def __init__(self, value):
        self._balance = value

    def pay(self, money):
        self._balance += money

    def take(self, money):
        if (self._balance - money) < 0:
            print("Brak wystarcząjacych środków na koncie!")
        else:
            self._balance -= money

    def show_balance(self):
        return self._balance

    def __str__(self):
        return f"Dostępne środki na koncie: {self.show_balance()} zł"


# część główna programu
if __name__ == '__main__':
    print(100*"-" + "\nZałożenie konta z saldem początkowym 1000 zł:")
    konto = Account(1000)
    print(konto)

    print(100 * "-" + "\nWpłata 200 zł:")
    konto.pay(200)
    print(konto)

    print(100 * "-" + "\nWypłata 500 zł:")
    konto.take(500)
    print(konto)

    print(100 * "-" + "\nWypłata 800 zł (ponad limit):")
    konto.take(800)
    print(konto)
