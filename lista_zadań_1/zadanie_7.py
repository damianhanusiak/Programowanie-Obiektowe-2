class TV:
    def __init__(self, channel, volume):
        self.channel = channel
        self.volume = volume

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, new_channel):
        if 1 <= new_channel <= 15:
            self._channel = new_channel
        else:
            print("Wybrano kanal spoza zakresu [1-15]!")
            self._channel = 1

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        if 1 <= new_volume <= 100:
            self._volume = new_volume
        else:
            print("Wybrano wartosc spoza zakresu [1-100]!")
            self._volume = 1


if __name__ == "__main__":
    print("Utworzenie TV o kanale 1 i glosnosci 50:")
    tv1 = TV(1, 50)
    print(f"Kanal: {tv1.channel}")
    print(f"Glosnosc: {tv1.volume}")

    print("Zmiana kanalu na 5, oraz glosnosci na 99: ")
    tv1.channel = 5
    tv1.volume = 99
    print(f"Kanal: {tv1.channel}")
    print(f"Glosnosc: {tv1.volume}")

    print("Wyjscie poza zakres kanalow i glosnosci: ")
    tv1.channel = 20
    tv1.volume = 120
    print(f"Kanal: {tv1.channel}")
    print(f"Glosnosc: {tv1.volume}")
