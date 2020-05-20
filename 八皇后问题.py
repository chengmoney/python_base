answer = []


def judge(x, y, coord):
    """判断坐标coord是否在已知道坐标（x，y）的横边，竖边和斜边上
    coord：需要判断的坐标
    x, y:已知的坐标
    """
    if coord[1] - coord[0] == y - x or coord[0] + coord[1] == y + x \
            or coord[0] == x or coord[1] == y:
        return True


class Checkerboard:
    def __init__(self, edge=8):
        self.edge = edge
        self.coordinate = [(x, y) for x in range(0, edge)
                           for y in range(0, edge)]
        self.state = 0
        self.coordinate_state = {i: 0 for i in self.coordinate}
        self.state_ls = []

    def getitem(self, x, y):
        return self.coordinate_state[(x, y)]

    def setitem(self, x, y, value=1):
        self.coordinate_state[(x, y)] = value

    def get_coordinate(self):
        return self.coordinate

    def chess_number(self, state=1):
        """找出状态为1的棋子个数"""
        chess = []
        for k, v in self.coordinate_state.items():
            if v == state:
                chess.append(k)
        self.state_ls = chess
        return len(chess)


class Chess:
    def __init__(self, coord):
        self.coord = coord
        self.scope = []

    def fall_down(self, chd):
        chd.setitem(*self.coord, 1)
        list_0 = find_place(chd)
        for _i in list_0:
            if judge(*self.coord, _i):
                self.scope.append(_i)
                chd.setitem(*_i, 2)

    def fall_up(self, chd):
        chd.setitem(*self.coord, 0)
        for _x in self.scope:
            chd.setitem(*_x, 0)


def change_state(x, y, chd):
    """将（x，y）坐标的横，纵，斜边的状态变为2
    状态2 表示棋子在（x，y）时候，后续的棋子不能放置在状态为2的地方
    """
    for cdt in chd.get_coordinate():
        # cdt需要判断的坐标点
        if judge(x, y, cdt):
            chd.setitem(cdt[0], cdt[1], 2)
    chd.setitem(x, y, 1)  # 将（x，y）的状态改边回来


def find_place(chd, state=0):
    """找出状态state为0或1或2 的棋盘坐标
state 默认为0
    """
    assert state in [0, 1, 2]
    state_0 = []
    for k, v in chd.coordinate_state.items():
        if v == state:
            state_0.append(k)
    return state_0


def find_place_x(chd, x, state=0):
    state_0_x = []
    for k, v in chd.coordinate_state.items():
        if v == state:
            if k[0] == x:
                state_0_x.append(k)
    return state_0_x


def is_answer(lt, chd, chess):
    if chd.chess_number() == 8:
        global answer
        answer.append(chd.state_ls)
        return False
    elif not lt:
        return False
    else:
        return True


def solve(chd):
    for i_1 in [(0, y) for y in range(8)]:
        chess1 = Chess(i_1)
        chess1.fall_down(chd)
        fp = find_place_x(chd, 1, 0)
        if is_answer(fp, chd, chess1):
            for i_2 in fp:
                chess2 = Chess(i_2)
                chess2.fall_down(chd)
                fp = find_place_x(chd, 2, 0)
                if is_answer(fp, chd, chess2):
                    for i_3 in fp:
                        chess3 = Chess(i_3)
                        chess3.fall_down(chd)
                        fp = find_place_x(chd, 3, 0)
                        if is_answer(fp, chd, chess3):
                            for i_4 in fp:
                                chess4 = Chess(i_4)
                                chess4.fall_down(chd)
                                fp = find_place_x(chd, 4, 0)
                                if is_answer(fp, chd, chess4):
                                    for i_5 in fp:
                                        chess5 = Chess(i_5)
                                        chess5.fall_down(chd)
                                        fp = find_place_x(chd, 5, 0)
                                        if is_answer(fp, chd, chess5):
                                            for i_6 in fp:
                                                chess6 = Chess(i_6)
                                                chess6.fall_down(chd)
                                                fp = find_place_x(chd, 6, 0)
                                                if is_answer(fp, chd, chess6):
                                                    for i_7 in fp:
                                                        chess7 = Chess(i_7)
                                                        chess7.fall_down(chd)
                                                        fp = find_place_x(chd, 7, 0)
                                                        if is_answer(fp, chd, chess7):
                                                            for i_8 in fp:
                                                                chess8 = Chess(i_8)
                                                                chess8.fall_down(chd)
                                                                fp = find_place(chd, 0)
                                                                if is_answer(fp, chd, chess8):
                                                                    pass
                                                                chess8.fall_up(chd); del chess8
                                                        chess7.fall_up(chd); del chess7
                                                chess6.fall_up(chd); del chess6
                                        chess5.fall_up(chd); del chess5
                                chess4.fall_up(chd); del chess4
                        chess3.fall_up(chd); del chess3
                chess2.fall_up(chd); del chess2
        chess1.fall_up(chd); del chess1


chboard = Checkerboard()
solve(chboard)











