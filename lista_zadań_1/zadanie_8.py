class Pet:
    def __init__(self, name, hunger=0, tiredness=0):
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            print("Podaj imie zwierzaka o poprawnej dlugosci!")
            self._name = "Burek"
        else:
            self._name = value

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    @property
    def mood(self):
        nastroj = self.hunger + self.tiredness
        if nastroj < 5:
            return "szczesliwy"
        elif 5 <= nastroj <= 10:
            return "zadowolony"
        elif 11 <= nastroj <= 15:
            return "podenerwowany"
        elif nastroj > 15:
            return "wsciekly"

    def talk(self):
        print(f"Zwierzak jest {self.mood}")
        self._passage_of_time()

    def eat(self, food=4):
        self.hunger -= food
        self._passage_of_time()

    def play(self, fun=4):
        self.tiredness -= fun
        self._passage_of_time()

    def __str__(self):
        return f"{self.name} | poziom glodu {self.hunger} | poziom znudzenia {self.tiredness}"


def main():
    # konkretyzacja obiektu klasy Pet
    zwierzak = Pet(input("Podaj nazwe swojego zwierzaka: "))

    while True:
        print(50*'-')
        print("1.Nastroj zwierzaka")
        print("2.Zmniejsz poziom glodu")
        print("3.Zmniejsz poziom znudzenia")
        print("4.Stan zwierzaka")
        print("5.Wyjdz")
        print(50*'-')

        choice = int(input("Twoj wybor: "))
        if choice == 1:
            zwierzak.talk()
        elif choice == 2:
            jedzenie = int(input("Ile jedzenia chesz dac zwierzakowi?"))
            zwierzak.eat(jedzenie)
        elif choice == 3:
            czas = int(input("Ile czasu chcesz sie bawic ze zwierzakiem?"))
            zwierzak.play(czas)
        elif choice == 4:
            print(zwierzak)
        elif choice == 5:
            break
        else:
            print("Nie ma takiej opcji!")


if __name__ == '__main__':
    main()
