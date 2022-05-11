import random


class Die:
    def __init__(self, sides):
        self._sides = sides  # liczba ścian kostki
        self._value = None  # wylosowana liczba oczek

    def roll(self):
        """wykonuje rzut kostką i wynik rzutu przypisuje do atrybutu value"""
        self._value = random.randint(1, self._sides)

    def get_sides(self):
        """zwraca liczbę ścianek"""
        return self._sides

    def get_value(self):
        """zwraca liczbę oczek na kostce"""
        return self._value


def gra():
    die1 = Die(6)
    die2 = Die(6)

    player_points = 0
    pc_points = 0

    def throw():
        die1.roll()
        die2.roll()

        return die1.get_value() + die2.get_value()

    while True:
        while player_points <= 21:
            if input("Czy chcesz rzucic? [t/n]") != "t":
                break

            t = throw()
            player_points += t
            print("Wyrzuciles ", t, "punktow")
            if pc_points <= 18:
                pc_points += throw()

        print("Zdobyles ", player_points, "punktow")
        print("Komputer zdobyl", player_points, "punktow")

        if (player_points <= 21 and pc_points <= 21) or (player_points >= 21 and pc_points >= 21):
            if player_points > pc_points:
                print("Wygrales")
            elif pc_points > player_points:
                print("Przegrales")
            else:
                print("Remis")
        elif player_points > 21:
            print("Przegrales!")
        else:
            print("Przegrales")

        player_points = pc_points = 0

        if input("Zagraj jeszcze raz: [t/n]") != "t":
            break


if __name__ == '__main__':
    gra()
