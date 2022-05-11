import collections.abc as abc


def flatten(iterable, ignore=(str,)):
    for x in iterable:
        if isinstance(x, abc.Iterable) and not isinstance(x, ignore):
            for y in flatten(x, ignore):
                yield y
        else:
            yield x


nestedSeq = ([1, 'kot'], 3, (4, 5, [7, 8, 9]), {2, 3}, {'pies': 3, 'kot': 2})
print([x for x in flatten(nestedSeq)])
