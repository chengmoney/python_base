def conflict(state, next_y):
    """检测下一个棋子是否与前面的棋子有冲突
    state:棋子的状态
    next_y:检测的棋子所在行数
    """
    next_x = len(state)  # x的坐标
    for i in range(next_x):
        if abs(state[i] - next_y) in (0, next_x - i):
            # 在检测皇后与前面的皇后 y的差值为0时：水平（在同一行）；y的差值 = x的差值时候（为斜边）
            return True
    return False


def queens(num=8, state=()):
    """
    基线条件：当要放置最后一个皇后时，遍历所有可能的位置，返回不会引发冲突的位置
    :param num: 皇后的总数
    :param state: 皇后在棋盘上的状态
    :return: 不会引发冲突的位置
    """
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield (pos,)
    else:
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state + (pos,)):
                    yield result + (pos,)


list(queens(8))



