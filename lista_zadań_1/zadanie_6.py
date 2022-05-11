class RocketEngine:
    count = 0
    all_power = 0

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.working = False
        self.__class__.count += 1

    def start(self):
        if self.working == False:
            self.__class__.all_power += self.power
            self.working = True

    def stop(self):
        if self.working == True:
            self.__class__.all_power -= self.power
            self.working = False

    def __str__(self):
        if self.working == True:
            return f"Nazwa silnika: {self.name}\nMoc silnika: {self.power}\nStan: Włączony\n"
        else:
            return f"Nazwa silnika: {self.name}\nMoc silnika: {self.power}\nStan: Wyłączony\n"

    def __del__(self):
        self.__class__.count -= 1
        print(f"Usunięto silnik: {self.name}")

    @staticmethod
    def status():
        print(
            f"Liczba silnikow: {RocketEngine.count}\nMoc silnikow: {RocketEngine.all_power}")


if __name__ == '__main__':
    print(50*'-')
    RocketEngine.status()
    print(50*'-')

    print("Manewrowanie")
    manewrowy1 = RocketEngine("manewrowy1", 50)
    manewrowy2 = RocketEngine("manewrowy2", 50)
    manewrowy1.start()
    manewrowy2.start()
    print(manewrowy1)
    print(manewrowy2)
    RocketEngine.status()
    print(50*'-')

    print("Rozpedzanie")
    rozpedowy1 = RocketEngine("rozpedowy1", 500)
    rozpedowy2 = RocketEngine("rozpedowy2", 500)
    rozpedowy1.start()
    rozpedowy2.start()
    manewrowy1.stop()
    manewrowy2.stop()
    print(rozpedowy1)
    print(rozpedowy2)
    RocketEngine.status()
    print(50*'-')

    print("Hiperprędkość")
    szybki1 = RocketEngine("szybki1", 400000)
    szybki2 = RocketEngine("szybki2", 400000)
    szybki1.start()
    szybki2.start()
    rozpedowy1.stop()
    rozpedowy2.stop()
    print(szybki1)
    print(szybki2)
    RocketEngine.status()
    print(50*'-')

    print("Zwalnianie")
    rozpedowy1.start()
    rozpedowy2.start()
    szybki1.stop()
    szybki2.stop()
    del szybki1  # usuwanie niepotrzebnych już obiektów
    del szybki2
    RocketEngine.status()
    print(50*'-')

    print("Cumowanie i manewrowanie")
    manewrowy1.start()
    manewrowy2.start()
    rozpedowy1.stop()
    rozpedowy2.stop()
    del rozpedowy1
    del rozpedowy2
    RocketEngine.status()
    print("\nZatrzymanie\n")
    print(50*'-')

    manewrowy1.stop()
    manewrowy2.stop()
    del manewrowy1
    del manewrowy2
    RocketEngine.status()
    print(50*'-')
