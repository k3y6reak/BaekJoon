from collections import deque


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def possible_area(map_, x, y, R, C):
    move_cnt = 0

    # 상, 하, 좌, 우 확산이 가능한 구역을 확인한다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 밖이거나, 공기청정기가 있는 위치면 확산하지 못한다.
        if nx < 0 or ny < 0 or nx >= R or ny >= C or map_[nx][ny] == -1:
            continue

        move_cnt += 1

    # 이동 가능한 영역의 개수를 구한다.
    return move_cnt


def dust_move(map_, dust_list, R, C):
    tmp_map = [[0]*C for _ in range(R)]

    # 먼지 리스트를 하나씩 꺼내고, 상, 하, 좌, 우 확산시킨다.
    for dust in dust_list:
        x = dust[0]
        y = dust[1]

        move_cnt = possible_area(map_, x, y, R, C)

        # 상, 하, 좌, 우로 확산한다.
        dust_cnt = map_[x][y] // 5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이거나, 공기청정기가 있는 위치면 확산하지 못한다.
            if nx < 0 or ny < 0 or nx >= R or ny >= C or map_[nx][ny] == -1:
                continue

            tmp_map[nx][ny] += dust_cnt

        tmp_map[x][y] += map_[x][y] - dust_cnt * move_cnt

    # 확산된 먼지를 맵에 적용시킨다.
    for r in range(R):
        for c in range(C):
            tmp = tmp_map[r][c]
            if tmp != 0:
                map_[r][c] = tmp_map[r][c]

    return map_


def set_dust(map_, R, C):
    dust_sum = 0
    dust_list = []

    for r in range(R):
        for c in range(C):
            if map_[r][c] != 0 and map_[r][c] != -1:
                dust_sum += map_[r][c]
                dust_list.append((r, c))

    return dust_sum, dust_list


def air_move(map_, air_list, R, C):

    # 공기 청정기가 위치한 열을 이동시킨다.
    map_[air_list[0][0] - 1][0] = 0
    for idx in range(air_list[0][0] - 1, 0, -1):
        map_[idx][0] = map_[idx - 1][0]
        map_[idx - 1][0] = 0

    map_[air_list[1][0] + 1][0] = 0
    for idx in range(air_list[1][0] + 2, R):
        map_[idx - 1][0] = map_[idx][0]
        map_[idx][0] = 0

    # 첫 행과 마지막 행을 이동시킨다.
    for idx in range(1, C):
        map_[0][idx-1] = map_[0][idx]
        map_[0][idx] = 0
        map_[R-1][idx-1] = map_[R-1][idx]
        map_[R-1][idx] = 0

    # 마지막 열을 이동시킨다.
    for idx in range(0, air_list[0][0]):
        map_[idx][C-1] = map_[idx + 1][C-1]
        map_[idx + 1][C-1] = 0

    for idx in range(R-1, air_list[1][0], -1):
        map_[idx][C-1] = map_[idx-1][C-1]
        map_[idx-1][C-1] = 0

    # 공기청정기 행을 이동시킨다.
    for idx in range(C-2, 0, -1):
        map_[air_list[0][0]][idx+1] = map_[air_list[0][0]][idx]
        map_[air_list[0][0]][idx] = 0
        map_[air_list[1][0]][idx+1] = map_[air_list[1][0]][idx]
        map_[air_list[1][0]][idx] = 0

    dust_sum, dust_list = set_dust(map_, R, C)

    return map_, dust_sum, dust_list


def main():
    R, C, T = map(int, input().split())

    map_ = [[0]*C for _ in range(R)]
    dust_list = []
    air_list = []
    dust_sum = 0

    # 맵을 만들고, 먼지위치, 공기청정기 위치를 뽑아낸다.
    for r in range(R):
        tmp = input().split()

        for idx, t in enumerate(tmp):
            t = int(t)

            if t == -1:
                air_list.append((r, idx))

            elif t != 0:
                dust_list.append((r, idx))

            map_[r][idx] = t

        map_[r] = deque(map_[r])

    # 먼지과 바람을 이동시킨다.
    for time in range(T):
        map_ = dust_move(map_, dust_list, R, C)
        map_, dust_sum, dust_list = air_move(map_, air_list, R, C)

    print(dust_sum)


if __name__ == '__main__':
    main()
