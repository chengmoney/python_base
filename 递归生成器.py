def flanten(nls):
    try:
        for sbl in nls:
            for ls in flanten(sbl):
                yield ls
    except TypeError:
        yield nls


lst = [[1, 2], 1, 2, [5, [7, 8]]]
for i in flanten(lst):
    print(i)
    if not i:
        break
