ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5


def get_5_line(N):
    """
    주어진 조건에 따른 x, y, d1, d2 값을 선정한다.
    :param N: 범위
    :return: 조건에 따른 x, y, d1, d2 값
    """

    possible_area = []

    for x in range(N):
        for y in range(N):
            for d1 in range(N):
                for d2 in range(N):
                    if x < x + d1 + d2 < N and 0 <= y-d1 < y < y+d2 < N:
                        possible_area.append([x, y, d1, d2])

    return possible_area


def set_up_left_line(area_map, x, y, d1, d2):
    """
    위에서부터 왼쪽으로 진행하는 경계선을 설정하는 함수
    :param area_map: 지역구를 설정하는 맵
    :param x: 조건에 따른 x
    :param y: 조건에 따른 y
    :param d1: 조건에 따른 d1
    :param d2: 조건에 다른 d2
    :return: 경계가 설정된 맵, 설정된 좌표
    """

    # 위 왼쪽 방향 경계선을 만든다.
    x_range = list(range(x, x + d1 + 1))
    y_range = list(range(y, y - d1 - 1, -1))

    len_ = min(len(x_range), len(y_range))

    # 경계 내부도 설정하기 위해 좌표 저장.
    xy = []

    for i in range(len_):
        area_map[x_range[i]][y_range[i]] = FIVE
        xy.append([x_range[i], y_range[i]])

    return area_map, xy[:-1]


def set_up_right_line(area_map, x, y, d1, d2):
    """
    위에서부터 오른쪽으로 진행하는 경계선을 설정하는 함수
    :param area_map: 지역구를 설정하는 맵
    :param x: 조건에 따른 x
    :param y: 조건에 따른 y
    :param d1: 조건에 따른 d1
    :param d2: 조건에 다른 d2
    :return: 경계가 설정된 맵
    """

    # 위 오른쪽 방향 경계선을 만든다.

    x_range = list(range(x, x + d2 + 1))
    y_range = list(range(y, y + d2 + 1))

    len_ = min(len(x_range), len(y_range))

    for i in range(len_):
        area_map[x_range[i]][y_range[i]] = FIVE

    return area_map


def set_down_right_line(area_map, x, y, d1, d2):
    """
    아래에서 오른쪽으로 진행하는 경계선을 설정하는 함수
    :param area_map: 지역구를 설정하는 맵
    :param x: 조건에 따른 x
    :param y: 조건에 따른 y
    :param d1: 조건에 따른 d1
    :param d2: 조건에 다른 d2
    :return: 경계가 설정된 맵
    """

    # 아래 오른쪽 방향 경계선을 만든다.

    x_range = list(range(x + d1, x + d1 + d2 + 1))
    y_range = list(range(y - d1, y - d1 + d2 + 1))

    len_ = min(len(x_range), len(y_range))

    for i in range(len_):
        area_map[x_range[i]][y_range[i]] = FIVE

    return area_map


def set_down_left_line(area_map, x, y, d1, d2):
    """
    아래에서 왼쪽으로 진행하는 경계선을 설정하는 함수
    :param area_map: 지역구를 설정하는 맵
    :param x: 조건에 따른 x
    :param y: 조건에 따른 y
    :param d1: 조건에 따른 d1
    :param d2: 조건에 다른 d2
    :return: 경계가 설정된 맵, 설정된 좌표
    """

    # 아래 왼쪽 방향 경계선을 만든다.

    x_range = list(range(x + d2, x + d1 + d2 + 1))
    y_range = list(range(y + d2, y + d2 - d1 - 1, -1))

    len_ = min(len(x_range), len(y_range))

    xy = []

    for i in range(len_):
        area_map[x_range[i]][y_range[i]] = FIVE
        xy.append([x_range[i], y_range[i]])

    return area_map, xy


def set_1_area(area_map, x, y, d1, d2):
    """
    1번 지역구를 설정하는 함수
    :param area_map: 지역구를 설정하는 맵
    :param x: 조건에 따른 x
    :param y: 조건에 따른 y
    :param d1: 조건에 따른 d1
    :param d2: 조건에 따른 d2
    :return: 1번 지역구가 추가된 맵
    """

    for i in range(x + d1):
        for j in range(y + 1):
            if area_map[i][j] != FIVE:
                area_map[i][j] = ONE

    return area_map


def set_2_area(area_map, x, y, d1, d2):
    """
    2번 지역구를 설정하는 함수
    :param area_map: 지역구를 설정하는 맵
    :param x: 조건에 따른 x
    :param y: 조건에 따른 y
    :param d1: 조건에 따른 d1
    :param d2: 조건에 따른 d2
    :return: 2번 지역구가 추가된 맵
    """

    for i in range(x + d2 + 1):
        for j in range(y+1, len(area_map)):
            if area_map[i][j] != FIVE:
                area_map[i][j] = TWO

    return area_map


def set_3_area(area_map, x, y, d1, d2):
    """
    3번 지역구를 설정하는 함수
    :param area_map: 지역구를 설정하는 맵
    :param x: 조건에 따른 x
    :param y: 조건에 따른 y
    :param d1: 조건에 따른 d1
    :param d2: 조건에 따른 d2
    :return: 3번 지역구가 추가된 맵
    """

    for i in range(x + d1, len(area_map)):
        for j in range(y - d1 + d2):
            if area_map[i][j] != FIVE:
                area_map[i][j] = THREE

    return area_map


def set_4_area(area_map, x, y, d1, d2):
    """
    4번 지역구를 설정하는 함수
    :param area_map: 지역구를 설정하는 맵
    :param x: 조건에 따른 x
    :param y: 조건에 따른 y
    :param d1: 조건에 따른 d1
    :param d2: 조건에 따른 d2
    :return: 4번 지역구가 추가된 맵
    """

    for i in range(x + d2 + 1, len(area_map)):
        for j in range(y - d1 + d2, len(area_map)):
            if area_map[i][j] != FIVE:
                area_map[i][j] = FOUR

    return area_map


def set_5_area(area_map, left_xy, right_xy):
    """
    경계선 내부에 존재하는 지역구를 세팅하는 함수.
    :param area_map: 지역구를 설정하는 맵
    :param left_xy: 위에서 왼쪽으로 내려가는 좌표
    :param right_xy: 아래에서 왼쪽으로 내려가는 좌표. (위치상 오른쪽)
    :return:
    """

    for idx in range(len(left_xy)):
        x = left_xy[idx][0]
        y = left_xy[idx][1]

        # 지그재그로 내려가면서 끝나는 좌표를 만날때 까지 세팅한다.
        while not(x == right_xy[idx][0] and y == right_xy[idx][1]):
            # 아래로 이동한다.
            x += 1
            area_map[x][y] = FIVE

            # 오른쪽으로 이동한다.
            y += 1
            area_map[x][y] = FIVE

    return area_map


def get_max_min(map_, area_map, N):
    """
    지역구들에 존재하는 인원을 파악하고, 최대 인원과 최소 인원의 차를 구하는 함수.
    :param map_: 인원이 세팅된 맵
    :param area_map: 지역구가 세팅된 맵
    :param N: 맵의 범위
    :return: 최대 인원과 최소 인원의 차이
    """
    area_sum = [0, 0, 0, 0, 0]

    for i in range(N):
        for j in range(N):
            area = area_map[i][j]

            area_sum[area - 1] += map_[i][j]

    return max(area_sum) - min(area_sum)


def main():
    N = int(input())

    map_ = [[int(i) for i in input().split()] for _ in range(N)]

    possible_area = get_5_line(N)

    total_min = 99999999

    for possible in possible_area:
        area_map = [[0] * N for _ in range(N)]

        x = possible[0]
        y = possible[1]
        d1 = possible[2]
        d2 = possible[3]

        # 5번 선거구 라인 설정
        left_five_xy = []
        area_map, xy = set_up_left_line(area_map, x, y, d1, d2)
        left_five_xy.extend(xy)

        area_map = set_up_right_line(area_map, x, y, d1, d2)
        area_map = set_down_right_line(area_map, x, y, d1, d2)

        right_five_xy = []
        area_map, xy = set_down_left_line(area_map, x, y, d1, d2)
        right_five_xy.extend(xy)

        # 5번 선거구 라인 내 설정
        area_map = set_5_area(area_map, left_five_xy, right_five_xy)

        area_map = set_1_area(area_map, x, y, d1, d2)
        area_map = set_2_area(area_map, x, y, d1, d2)
        area_map = set_3_area(area_map, x, y, d1, d2)
        area_map = set_4_area(area_map, x, y, d1, d2)

        calc = get_max_min(map_, area_map, N)

        total_min = min(total_min, calc)

    print(total_min)


if __name__ == '__main__':
    main()
