def get_number(a, b, text):
    """Funkcja pobiera liczbę całkowitą z zakresu a-b"""
    while True:
        try:
            data = input(f"{text} (zakres: {a} - {b}): ")
            n = int(data)
            if a <= n <= b: # n >= a and n <=b
                return n
            else:
                print("Liczba poza zakresem!")
        except ValueError:
            print(f"{data} - to nie jest liczba całkowita!")

def lay_mines(number_of_mines, rows, collums):
    """Funkcja zwraca zbiór współrzędnych min"""
    import random
    mines = set()
    while len(mines) < number_of_mines:
        i = random.randint(0,rows)
        j = random.randint(0,collums)
        mines.add((i,j))
    return mines

def number_of_neighboring_mines(field, mines):
    """opis"""
    i = field[0]
    j = field[1]
    count = 0
    for x in [(i-1,j-1), (i-1,j), (i-1,j+1),
              (i,i-1),(i,j+1),
              (i+1,j-1), (i+1,j), (i+1,j+1)]:
        if x in mines:
            count += 1
    return count

def create_board(rows, collums, mines, mine="*"):
    board = []
    for i in range(rows):
        row = []
        for j in range(collums):
            if (i, j) in mines:
                row.append(mine)
            else:
                row.append(number_of_neighboring_mines((i,j),mines))
        board.append(row)
    return board

def reveal_fields(field, printable_fields, rows, collums):
    i = field[0]
    j = field[1]
    if not (0 <= i < rows and 0 <= j < collums) or (i,j) in printable_fields:
        return

    printable_fields.add((i, j))
    if board[i][j] != 0:
        return
    else:
        for x in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                  (i, i - 1), (i, j + 1),
                  (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
            reveal_fields(x, printable_fields, board, rows, collums)

def print_board(printable_fields, board, rows, collums, all_print = False):
    print("  ", end='')
    for i in range(collums):
        print(f"{i:>4}", end='')
    print()
    for i in range(rows):
        print(f"{i:<4}", end='')
        for j in range(collums):
            if (i,j) in printable_fields or all_print:
                print(f"{board[i][j]} |", end='')
            else:
                print(f" # |", end='')
        print()

r = 10
c = 10
n = 10
s = lay_mines(n, r, c)
board = create_board(r, c, s)
printable_fields = set()

print_board(printable_fields,board,r,c)
i = get_number(0,r-1,"podaj nr wiersza")
j = get_number(0,c-1,"podaj nr kolumny")

if (i, j) not in s:
    reveal_fields((i,j),printable_fields,board,r,c)