class Pupil:
    ratings = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = {}

    @property
    def name(self):
        return self.__dict__["name"]

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
            self.__dict__["name"] = new_name
        else:
            print(
                "Imie musi posiadac przynajmniej 3 znaki i byc typu tekstowego! Nadano domyslne imie!")
            self.__dict__["name"] = "NoName"

    @property
    def surname(self):
        return self.__dict__["surname"]

    @surname.setter
    def surname(self, new_surname):
        if isinstance(new_surname, str) and len(new_surname) >= 3:
            self.__dict__["surname"] = new_surname
        else:
            print(
                "Nazwisko musi posiadac przynajmniej 3 znaki i byc typu tesktowego! Nadano domyslne nazwisko!")
            self.__dict__["surname"] = "NoSurname"

    # def complete_marks(self, subject, rating):
    def print_marks(self):
        for i in self.marks:
            print(f"{i}: {self.marks[i]}")

    def mean(self):
        sum = 0
        count = 0
        for i in self.marks:
            count += 1
            sum += self.marks[i]
        return sum / count

    def __str__(self):
        return f"Imie: {self.name}, Nazwisko: {self.surname}, Średnia ocen: {self.mean()}"


class Student(Pupil):
    weights_range = (0, 1)

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.weights = {}
