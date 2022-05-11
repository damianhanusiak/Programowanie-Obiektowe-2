from zadanie_1_moduł import Note, Notebook
import sys


class Menu(object):

    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def show_menu(self):
        print("\n[1] Pokaż wszystkie notatki,\n[2] Szukaj notatki,\n[3] Dodaj notatkę,"
              "\n[4] Modyfikuj notatkę,\n[5] Wyjdź")

    def run(self, option):
        self.options[option]()

    def show_notes(self):
        print(self.notebook)

    def search_notes(self):
        szukana = input("Podaj szukaną frazę(tag):")
        for x in self.notebook.search(szukana):
            print(x)

    def add_note(self):
        tag = input("Podaj tag notatki:\t")
        text = input("Podaj tekst notatki:\t")
        notatka = Note(text, tag)
        self.notebook.new_note(notatka)

    def modify_note(self):
        number = int(input("Podaj ID notatki do zmiany:\t"))
        what = int(input("[1] Zmień tag notatki,\n[2] Zmień tekst notatki"))
        if what == 1:
            tag = input("Podaj nowy tag notatki:\t")
            self.notebook.modify_tag(number, tag)
        else:
            text = input("Podaj nowy tekst notatki:\t")
            self.notebook.modify_text(number, text)

    def quit(self):
        sys.exit()


if __name__ == '__main__':
    menu = Menu()
    while True:
        menu.show_menu()
        what = input("Wybierz opcje:\t")
        if what in menu.options:
            menu.run(what)
        else:
            print("Nie ma takiego wyniku!!!")
