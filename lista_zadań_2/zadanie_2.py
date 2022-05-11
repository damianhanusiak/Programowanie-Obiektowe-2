import math

class Figure:
    def __init__(self, colour='red', is_filled=True):
        self.colour = colour
        self.is_filled = is_filled

    def __str__(self):
        return f"Kolor: {self.colour}, Wypełniony: {self.is_filled}"

    def __repr__(self):
        return f"{type(self).__name__}"\
            f"(" + ', '.join((f'{v} = {k!r}' for v,
                              k in self.__dict__.items())) + ')'


class Circle(Figure):
    def __init__(self, colour='red', is_filled=True, radius=5):
        super().__init__(colour, is_filled)
        self.radius = radius
        self.area = math.pi * math.pow(self.radius, 2)
        self.perimeter = 2 * math.pi * self.radius
        self.diameter = 2 * self.radius

    @property
    def radius(self):
        return self.__dict__["radius"]

    @radius.setter
    def radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self.__dict__["radius"] = new_radius
        else:
            self.__dict__["radius"] = 2.0 

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value):
        self._perimeter = value

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value

    def __str__(self):
        return super().__str__() + f", Promień: {self.radius}, Pole: {self.area}, Obwod: {self.perimeter}, Srednica: {self.diameter}"

    def __repr__(self):
        return super().__repr__()


class Rectangle(Figure):
    def __init__(self, colour='red', is_filled=True, width=1, height=2):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = 2*self.width + 2*self.height
        self.diagonal = math.sqrt(
            math.pow(self.height, 2) + math.pow(self.height, 2))

    @property
    def width(self):
        return self.__dict__["width"]

    @width.setter
    def width(self, value):
        if isinstance(value, float) and value > 0:
            __dict__["width"] = value
        else:
            __dict__["width"] = 1.0

    @property
    def height(self):
        return self.__dict__["height"]

    @height.setter
    def height(self, value):
        if isinstance(value, float) and value > 0:
            self.__dict__["height"] = value
        else:
            self.__dict__["height"] = 2.0

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value):
        self._perimeter = value

    @property
    def diagonal(self):
        return self._diagonal

    @diagonal.setter
    def diagonal(self, value):
        self._diagonal = value

    def __str__(self):
        return super().__str__() + f", Szerokosc: {self.width}, Wysokosc: {self.height}, Pole: {self.area}, Obwod: {self.perimeter}, Przekatna: {self.diagonal}"

    def __repr__(self):
        return super().__repr__()


if __name__ == '__main__':
    print(100*'-')
    figura = Figure()
    print(figura)
    print(repr(figura))

    print(100*'-')
    kolo = Circle('blue', True, 3.0)
    print(kolo)
    print(repr(kolo))

    print(100*'-')
    prostokat = Rectangle('red', False, 3.0, 5.0)
    print(prostokat)
    print(repr(prostokat))

    print(100*'-')
    print(Figure.__dict__)
    print(Circle.__dict__)
    print(Rectangle.__dict__)
