LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dust_move(map_, x, y, arrow, N):
    out_dust = 0

    if map_[x][y] == 0:
        return out_dust

    points = None
    rx = 0
    ry = 0

    if arrow == LEFT:
        points = [
            [0, -2, 5],
            [-1, -1, 10], [1, -1, 10],
            [-1, 0, 7], [1, 0, 7],
            [-2, 0, 2], [2, 0, 2],
            [-1, 1, 1], [1, 1, 1],
        ]

        rx = 0
        ry = -1

    elif arrow == DOWN:
        points = [
            [2, 0, 5],
            [1, -1, 10], [1, 1, 10],
            [0, -1, 7], [0, 1, 7],
            [0, -2, 2], [0, 2, 2],
            [-1, -1, 1], [-1, 1, 1]
        ]

        rx = 1
        ry = 0

    elif arrow == RIGHT:
        points = [
            [0, 2, 5],
            [-1, 1, 10], [1, 1, 10],
            [-1, 0, 7], [1, 0, 7],
            [-2, 0, 2], [2, 0, 2],
            [-1, -1, 1], [1, -1, 1]
        ]

        rx = 0
        ry = 1

    elif arrow == UP:
        points = [
            [-2, 0, 5],
            [-1, -1, 10], [-1, 1, 10],
            [0, -1, 7], [0, 1, 7],
            [0, -2, 2], [0, 2, 2],
            [1, -1, 1], [1, 1, 1]
        ]

        rx = -1
        ry = 0

    original_dust = map_[x][y]
    dust = map_[x][y]

    # 해당 방향으로 퍼지는 먼지 이동시킨다.
    for i, j, per in points:
        tmp_dust = int(original_dust * (0.01 * per))

        dust -= tmp_dust

        if x + i < 0 or y + j < 0 or x + i >= N or y + j >= N:
            out_dust += tmp_dust
            continue

        map_[x+i][y+j] += tmp_dust

    if x + rx < 0 or y + ry < 0 or x + rx >= N or y + ry >= N:
        out_dust += dust

    else:
        map_[x + rx][y + ry] += dust

    map_[x][y] = 0

    return out_dust


def move(x, y, arrow):
    x = x + dx[arrow]
    y = y + dy[arrow]

    return x, y


def main():
    N = int(input())

    map_ = [[int(n) for n in input().split()] for _ in range(N)]

    map2_ = [[0]*N for _ in range(N)]

    # 방향을 바꾸기 위한 배열
    #        좌, 하, 우, 상
    turns = [0, 0, 0, 0]

    arrow = LEFT

    # 중앙
    x = N//2
    y = N//2

    # 아래에서 오른쪽으로 변경되는 횟수
    cnt = 1

    out_dust = 0

    # 중앙부터 첫 지점까지 이동한다.
    while not (x == 0 and y == 0):

        if turns[LEFT] == cnt and turns[DOWN] == cnt:
            cnt += 1
            arrow = RIGHT
            turns[LEFT] = 0
            turns[DOWN] = 0

        elif turns[RIGHT] == cnt and turns[UP] == cnt:
            cnt += 1
            arrow = LEFT
            turns[RIGHT] = 0
            turns[UP] = 0

        if arrow == LEFT:
            if turns[LEFT] != cnt:
                turns[LEFT] += 1

            else:
                arrow = DOWN
                turns[DOWN] += 1

        elif arrow == DOWN:
            if turns[DOWN] != cnt:
                turns[DOWN] += 1

        elif arrow == RIGHT:
            if turns[RIGHT] != cnt:
                turns[RIGHT] += 1

            else:
                arrow = UP
                turns[UP] += 1

        elif arrow == UP:
            if turns[UP] != cnt:
                turns[UP] += 1

        x, y = move(x, y, arrow)

        out_dust += dust_move(map_, x, y, arrow, N)

    print(out_dust)


if __name__ == '__main__':
    main()
