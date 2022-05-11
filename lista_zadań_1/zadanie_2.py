from random import choice


class Coin:
    def __init__(self):
        self.side = None

    def throw(self):
        self.side = choice(["orzel", "reszka"])

    def show_side(self):
        return self.side


def main_a():
    print(40 * "-")
    print("Utworzenie kilku obiektów klasy Coin i wywołanie ich metod:")
    coin1 = Coin()
    coin2 = Coin()
    coin3 = Coin()
    coin4 = Coin()
    coin1.throw()
    coin2.throw()
    coin3.throw()
    coin4.throw()
    print(f"Obiekt 1: {coin1.show_side()}")
    print(f"Obiekt 2: {coin2.show_side()}")
    print(f"Obiekt 3: {coin3.show_side()}")
    print(f"Obiekt 4: {coin4.show_side()}")

    print(40 * "-")
    print("Symulacja 15 rzutów kostką:")
    coin = Coin()
    for i in range(15):
        coin.throw()
        print(f"Rzut {i + 1}: {coin.show_side()}")
    print(40 * "-")


def game_b():
    saldo = 0

    while saldo < 20:
        for i in range(3):
            coins = [Coin() for i in range(3)]
            for coin in coins:
                coin.throw()
                if coin.show_side() == "orzel":
                    if coins.index(coin) == 0:
                        saldo += 1
                    elif coins.index(coin) == 1:
                        saldo += 2
                    else:
                        saldo += 5

    print(f"Twoje saldo: {saldo}")
    if saldo == 20:
        return True
    return False


def main_b():
    wygrane = 0
    przegrane = 0
    for i in range(100):
        print(f"Gra - {i}")
        if(game_b()):
            wygrane += 1
        else:
            przegrane += 1

    print(f"Wygrane gry: {wygrane}")
    print(f"Przegrane gry: {przegrane}")


main_a()
main_b()
