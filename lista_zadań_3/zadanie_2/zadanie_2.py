def generator_calkowite():
    i = 0
    while True:
        yield i
        i += 1


def generator_kwadraty():
    for liczba in generator_calkowite():
        yield liczba ** 2


def select(obiekt, n):
    lista = []
    iterator = iter(obiekt)
    for i in range(n):
        try:
            lista.append(next(iterator))
        except StopIteration:
            break
    return lista


if __name__ == '__main__':
    print(select(generator_calkowite(), 15))
    print(select(generator_kwadraty(), 15))

    trojki = ((a, b, c)for c in generator_calkowite() for b in range(1, c)
              for a in range(1, b) if a ** 2 + b ** 2 == c ** 2)
    print(select(trojki, 15))
