class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def __str__(self):
        return f"Dlugosc: {self.length}, Wysokosc: {self.height}, Pole: {self.area()}"

    def __repr__(self):
        return f"{type(self).__name__}"\
            f"(" + ', '.join((f'{v} = {k!r}' for v,
                              k in self.__dict__.items())) + ')'


class Cuboid(Rectangle):
    def __init__(self, length, height, width):
        super().__init__(length, height)
        self.width = width

    def area(self):
        # return super().area()*2 + 2*self.length*self.width + 2*self.height*self.width
        return 2*(super().area() + self.length*self.width + self.height*self.width)

    def volume(self):
        return super().area()*self.width

    def __str__(self):
        return super().__str__() + f", Szerokosc: {self.width}, Objetosc: {self.volume()}"

    def __repr__(self):
        return super().__repr__()


class InvalidData(Exception):
    pass


if __name__ == '__main__':

    filepath = "dane.txt"
    file = open(filepath, "r")

    for line in file:
        try:
            row = [int(x) for x in line.split()]
            if row[0] == 1 and len(row) == 3:
                if row[1] > 0 and row[2] > 0:
                    print(Rectangle(*row[1:]))
                    #rectangle = Rectangle(row[1],row[2])
                    # print(rectangle)
                else:
                    raise InvalidData("Ujemne wartosci!")
            elif row[0] == 2 and len(row) == 4:
                if row[1] > 0 and row[2] > 0 and row[3] > 0:
                    print(Cuboid(*row[1:]))
                    #cuboid = Cuboid(row[1], row[2], row[3])
                    # print(cuboid)
                else:
                    raise InvalidData("Ujemne wartosci!")
            else:
                raise InvalidData("Za duzo lub za malo danych!")

        except ValueError:
            print("Niepoprawne wartosci!")

        except InvalidData as Error:
            print(Error)

    file.close()
