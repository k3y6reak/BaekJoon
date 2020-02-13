from collections import deque
from itertools import islice

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

WHITE = 0
RED = 1
BLUE = 2


class Map:
    def __init__(self, color, current_unit):
        self.color = color
        self.current_unit = current_unit


class Unit:
    def __init__(self, idx, arrow, x, y):
        self.idx = idx
        self.arrow = arrow
        self.x = x
        self.y = y


def map_check(map_, N):
    """
    특정 위치에 유닛이 4개이상 존재하는지 확인하는 함수.
    :param map_: 맵
    :param N: 맵 크기
    :return: 4개이상 존재하면 True, 존재하지 않다면 False
    """

    for i in range(N):
        for j in range(N):
            if len(map_[i][j].current_unit) >= 4:
                return True

    return False


def map_range_check(N, next_x, next_y):
    """
    다음 위치가 맵 범위를 벗어나는지 체크하는 함수.
    :param N: 맵 크기
    :param next_x: 다음 x 위치
    :param next_y: 다음 y 위치
    :return:  범위 밖이면 False, 안이면 True
    """

    if next_x >= N or next_x < 0 or next_y >= N or next_y < 0:
        return False

    return True


def get_upper_unit(map_, unit, x, y):
    """
    특정 위치에 현재 유닛 위에 쌓인 유닛 전체를 가져오고, 깔린 유닛은 남겨두는 함수.
    :param map_: 맵
    :param unit: 현재 유닛
    :param x: 특정 위치 x
    :param y: 특정 위치 y
    :return: 현재 유닛을 포함한 위에 쌓인 유닛 전체.
    """
    
    # x, y 위치에 존재하는 전체 유닛을 가져온다.
    current_units = map_[x][y].current_unit

    # 현재 유닛부터 쌓여있는 유닛 전체를 가져온다.
    # 위 [1,2,3,4] 아래
    upper_unit = deque(islice(current_units, 0, current_units.index(unit)+1))

    # 쌓여있는 유닛을 제외하고 깔린 유닛을 남겨둔다.
    map_[x][y].current_unit = deque(islice(current_units, current_units.index(unit)+1, len(current_units)))

    return upper_unit


def get_next_map(map_, x, y):
    """
    
    :param map_: 맵 
    :param x: 특정 위치 x
    :param y: 특정 위치 y
    :return: xy 맵 정보
    """
    return map_[x][y]


def get_next_xy(x, y, arrow):
    """

    :param x: 현재 위치 x
    :param y: 현재 위치 y
    :param arrow: 이동하는 방향
    :return: 다음 위치의 x, y
    """
    next_x = 0
    next_y = 0

    # 방향이 왼쪽이거나 오른쪽이면 y의 값만 변경하면 된다.
    if arrow == LEFT or arrow == RIGHT:
        next_x = x
        if arrow == LEFT:
            next_y = y - 1
        else:
            next_y = y + 1

    # 방향이 위거나 아래면 x의 값만 변경하면 된다.
    elif arrow == UP or arrow == DOWN:
        next_y = y

        if arrow == UP:
            next_x = x - 1
        else:
            next_x = x + 1

    return next_x, next_y


def set_units_xy(upper_units, x, y):
    """
    쌓인 유닛을 옮기면서 각 유닛들의 위치를 재설정하는 함수.
    :param upper_units: 쌓인 유닛들.
    :param x: 이동하려는 x
    :param y: 이동하려는 y
    :return: None
    """

    for unit in upper_units:
        unit.x = x
        unit.y = y


def reverse_arrow(unit):
    """
    이동하는 방향의 반대 방향으로 설정하는 함수.
    :param unit: 특정 유닛
    :return: None
    """

    # 현재 방향이 홀수(오른쪽, 위) 방향이면 짝수(왼쪽, 아래) 방향으로 변경.
    if unit.arrow % 2 == 1:
        unit.arrow += 1
    else:
        unit.arrow -= 1


def move(map_, unit, N):
    """
    유닛을 이동시키는 함수.
    :param map_: 맵
    :param unit: 현재 유닛
    :param N: 맵의 크기
    :return: None
    """

    # 현재 유닛의 x, y 좌표를 가져온다.
    current_x = unit.x
    current_y = unit.y

    # 다음 위치의 좌표를 가져온다.
    next_x, next_y = get_next_xy(current_x, current_y, unit.arrow)

    # 다음 위치가 범위 밖이면 그 반대 방향으로 변경.
    if not map_range_check(N, next_x, next_y):
        reverse_arrow(unit)
        move(map_, unit, N)

    else:
        # 현재 위치의 말을 가져온다.
        upper_units = get_upper_unit(map_, unit, current_x, current_y)

        # 다음 위치의 맵 정보를 가져온다.
        next_map_info = get_next_map(map_, next_x, next_y)

        # 다음 위치의 색상 정보를 가져온다.
        next_map_color = next_map_info.color

        # 다음 위치가 하얀색인 경우.
        if next_map_color == WHITE:
            # 다음 위치에 upper_units를 넣어준다.
            # extendleft 함수 이용 시, 반대로 넣어지므로 reverse 사용.
            upper_units.reverse()

            # 가져온 말들의 좌표를 변경.
            set_units_xy(upper_units, next_x, next_y)

            next_map_info.current_unit.extendleft(upper_units)

        # 다음 위치가 빨간색인 경우.
        elif next_map_color == RED:
            set_units_xy(upper_units, next_x, next_y)
            next_map_info.current_unit.extendleft(upper_units)

        # 다음 위치가 파란색인 경우.
        elif next_map_color == BLUE:
            # 방향을 반대로 바꾼다.
            reverse_arrow(unit)

            # upper_units가 다시 제자리에 들어가야 함.
            upper_units.reverse()
            map_[current_x][current_y].current_unit.extendleft(upper_units)

            next_x, next_y = get_next_xy(current_x, current_y, unit.arrow)

            # 범위 안이거나, 다음 위치가 파란색이 아닌 경우, 해당 위치로 이동한다.
            if not((not map_range_check(N, next_x, next_y)) or get_next_map(map_, next_x, next_y).color == BLUE):
                move(map_, unit, N)


def turn(map_, N, units):
    # 한 턴에 존재하는 유닛을 모두 이동시킨다.
    for unit in units:
        move(map_, unit, N)

        # 하나씩 움직이고, 한 공간에 4개 이상의 말이 있는지 확인한다.
        if map_check(map_, N):
            return True

    return False


def main():
    N, K = map(int, input().split())

    map_ = [[Map(int(_), deque()) for _ in input().split()] for _ in range(N)]

    units = []

    # 유닛 세팅
    for k in range(K):
        x, y, arrow = map(int, input().split())
        unit = Unit("u_" + str(k+1), arrow, x-1, y-1)
        units.append(unit)
        map_[x-1][y-1].current_unit = deque([unit])

    end_flag = False
    move_cnt = 0

    # 최대 1000번 턴.
    for i in range(1000):
        end_flag = turn(map_, N, units)

        move_cnt += 1

        if not end_flag:
            continue
        else:
            break

    if end_flag:
        print(move_cnt)
    else:
        print(-1)


if __name__ == '__main__':
    main()
