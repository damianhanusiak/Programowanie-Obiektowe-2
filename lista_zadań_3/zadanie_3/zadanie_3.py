import itertools


def FiboGen():
    a = 0
    b = 0
    while True:
        a, b = a+b, a
        yield a


start = 100000
stop = 100002
with open("zadanie_2.txt", "w") as file:
    for i in itertools.isslice(FiboGen(), start, stop):
        print(f"{start},Dlugosc: {len(str(i))}, Wartosc: {i}, file=file")
