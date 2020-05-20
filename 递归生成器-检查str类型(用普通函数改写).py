def flt(ls):
    result = []
    try:
        try: ls + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in ls:
            for i in flt(sublist):
                result.append(i)
    except TypeError:
        result.append(ls)
    return result


#  ls = [[1, 2], 4, 5, [6, 7, [8, 9]]]
ls = [[1, 2], 'cheng']
print(flt(ls))


