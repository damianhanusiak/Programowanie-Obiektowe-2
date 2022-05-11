import numbers


class Person:
    def __init__(self, name=None, surname=None, age=None):
        self.name = name
        self.surname = surname
        self.age = age

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
                "Nazwisko musi posiadac przynajmniej 3 znaki i byc typu tekstowego! Nadano domyslne nazwisko!")
            self.__dict__["surname"] = "NoSurname"

    @property
    def age(self):
        return self.__dict__["age"]

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, numbers.Integral) and 0 <= new_age <= 130:
            self.__dict__["age"] = int(new_age)
        else:
            print("Wiek wykracza poza zakres zakres! Nadano domyslny wiek!")
            self.__dict__["age"] = 18

    def __str__(self):
        return f"Imie: {self.name}\nNazwisko: {self.surname}\nWiek: {self.age}\n"


class Student(Person):
    def __init__(self, name, surname, age, field_of_study):
        super().__init__(name, surname, age)
        self.field_of_study = field_of_study
        self.student_book = {}

    def add_subject(self, subject, grade):
        self.student_book[subject] = grade

    def __str__(self):
        return super().__str__() + f"Kierunek studiów: {self.field_of_study}\n Oceny: " +\
            ", ".join(f'{v}: {k}' for v, k in self.student_book.items())


class Employee(Person):
    def __init__(self, name, surname, age, job_title, skills):
        super().__init__(name, surname, age)
        self.job_title = job_title
        self.skills = []

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)

    def __str__(self):
        return super().__str__() + f"Zawód: {self.job_title}\n Umiejetnosci: " + \
            ", ".join(f'{v}' for v in self.skills)


if __name__ == '__main__':
    while True:
        print("[1] - Student")
        print("[2] - Pracownik")
        print("[3] - Exit")
        x = input("Wybierz opcje: ")
        if(x == "1"):
            stud = Student(input("Podaj imie: "), input("Podaj nazwisko: "), int(
                input("Podaj wiek: ")), input("Podaj kierunek studiow: "))
            while(x := input("Podaj przedmiot: ")):  # przypisanie jednoczesne
                stud.add_subject(x, int(input("Podaj ocene: ")))
            print(stud)

        elif(x == "2"):
            pracownik = Employee(input("Podaj imie: "), input("Podaj nazwisko: "), int(
                input("Podaj wiek: ")), input("Podaj zawod: "), "elo")
            print(pracownik)
        elif(x == "3"):
            print("Koniec pogramu!")
            break
