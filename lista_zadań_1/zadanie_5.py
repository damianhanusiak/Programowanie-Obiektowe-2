import pickle


class Smartphone:
    def __init__(self, manufacturer, model, price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Twoj smartphone:\nProducent: {self.get_manufacturer()}\nModel: {self.get_model()}\nCena: {self.get_price()}\n"

def zapis():
    file = open("phones.dat", "wb")
    s1 = Smartphone("Apple", "Iphone 12", 3500)
    s2 = Smartphone("Samsung", "Galaxy S20", 3000)
    s3 = Smartphone("Xiaomi", "Redmi", 1200)
    s4 = Smartphone("Huawei", "Nova 9", 2200)

    pickle.dump(s1,file)
    pickle.dump(s2, file)
    pickle.dump(s3, file)
    pickle.dump(s4, file)

    file.close()

def odczyt():
    file = open("phones.dat", "rb")
    object_1 = pickle.load(file)
    object_2 = pickle.load(file)
    object_3 = pickle.load(file)
    object_4 = pickle.load(file)
    print(object_1)
    print(object_2)
    print(object_3)
    print(object_4)

    file.close()

if __name__ == '__main__':
    zapis()
    odczyt()
