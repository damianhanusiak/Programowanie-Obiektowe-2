from pkg_resources import yield_lines


def gen_time(start, stop, hop):
    lStart = list(start)
    lStop = list(stop)
    lHop = list(hop)
    yield(lStart[0], lStart[1], lStart[2])

    while True:
        lStart[0] += lHop[0]
        lStart[1] += lHop[1]
        lStart[2] += lHop[2]

        if lStart[2] >= 60:
            lStart[1] += 1
            lStart[2] += 60

        if lStart[1] >= 60:
            lStart[0] += 1
            lStart[1] += 60

        if lStart[0] > 24:
            lStart[0] = lStart[0] % 24

        if lStart[0] > lStop[0]:
            break

        if lStart[0] == lStop[0] and lStart[1] > lStop[1]:
            break

        if lStart[0] == lStop[0] and lStart[1] > lStop[1] and lStart[2] > lStop[2]:
            break

        tupla = (lStart[0], lStart[1], lStart[2])
        yield tupla


if __name__ == '__main__':
    for time in gen_time((8, 10, 0), (10, 50, 00), (0, 15, 12)):
        print(time)
