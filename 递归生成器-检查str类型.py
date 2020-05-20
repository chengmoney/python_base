def flt(ls):
    try:
        try:
            ls + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in ls:
            for i in flt(sublist):
                yield i
    except TypeError:
        yield ls


#  ls = [[1, 2], 4, 5, [6, 7, [8, 9]]]
ls = [[1, 2], 'cheng']
# print(list(flt(ls)))

for i in flt(ls):
    print(i)
