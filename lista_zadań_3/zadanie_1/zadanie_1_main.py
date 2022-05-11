import sys
import authorization_system


class Editor:
    def __init__(self):
        self.username = None
        self.options = {
            "a": self.login,
            "b": self.test,
            "c": self.change,
            "d": self.quit
        }

    def login(self):
        login = input("Podaj login: ")
        haslo = input("Podaj haslo: ")
        try:
            authorization_system.authenticator.login(login, haslo)
            self.username = login
        except authorization_system.IncorrectUsername:
            print("Niepoprawny nazwa uzytkownika!")
        except authorization_system.IncorrectPassword:
            print("Niepoprawne haslo!")

    def is_permitted(self, permission):
        try:
            return authorization_system.authorizor.check_permission(self.username, permission)
        except authorization_system.NotLoggedError:
            print("Uzytkownik nie jest zalogowany!")
            return False
        except authorization_system.NotPermittedError:
            print("Brak odpowiednich uprawnien!")
            return False
        except authorization_system.PermissionError:
            print("Nieznane uprawnienia!")
            return False

    def test(self):
        if self.is_permitted("test"):
            print("Testowanie...")

    def change(self):
        if self.is_permitted("change"):
            print("Zmienianie...")

    def quit(self):
        sys.exit()

    def run(self):
        print("---MENU---")
        print("[a] - Login")
        print("[b] - Test")
        print("[c] - Change")
        print("[d] - Exit")
        choice = input("Wybierz opcje: ")
        if not choice in self.options:
            print("Nie ma takiej opcji!")
        else:
            self.options[choice]()


def menu():
    edit = Editor()
    while True:
        edit.run()


if __name__ == '__main__':
    menu()
