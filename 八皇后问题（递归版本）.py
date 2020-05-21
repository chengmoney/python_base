def conflict(state, next_y):
    next_x = len(state)
    for i in range(len(state)):
        if abs(next_y - state[i]) in (0, next_x - i):
            return True
    else:
        return False


def queens(num=8, state=()):
    if len(state) == num - 1:
        for _y in range(num):
            if not conflict(state, _y):
                yield (_y,)
    else:
        for y in range(num):
            if not conflict(state, y):
                for answer in queens(num, state+(y,)):
                    yield (y, ) + answer


list(queens(4))



