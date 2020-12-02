from collections import deque
from itertools import product


def find_big_ice(ice_map, map_size):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [[False]*map_size for _ in range(map_size)]

    q = deque()

    big_ice = 0

    for i in range(map_size):
        for j in range(map_size):

            # 얼음이 없거나 이미 방문한 곳이면 확인할 필요가 없다.
            if ice_map[i][j] == 0 or visited[i][j]:
                continue

            else:
                cnt = 1
                q.append([i, j])
                visited[i][j] = True

                # 해당 지점부터 얼음의 크기를 구한다.
                while len(q) != 0:
                    p = q.popleft()

                    x, y = map(int, p)

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or ny < 0 or nx >= map_size or ny >= map_size or visited[nx][ny] or ice_map[nx][ny] == 0:
                            continue

                        q.append([nx, ny])
                        visited[nx][ny] = True
                        cnt += 1

                big_ice = max(big_ice, cnt)

    print(big_ice)


def sum_ice(ice_map, map_size):
    ice_cnt = 0

    for i in range(map_size):
        ice_cnt += sum(ice_map[i])

    print(ice_cnt)


def divide_and_turn_map(ice_map, fire_storm, map_size):
    points = []

    # 구역별 첫번째 지점의 좌표값을 찾는다.
    point = 0
    while point < map_size:
        points.append(point)
        point += (2**fire_storm)

    # 해당 지점을 기준으로 90도 회전시킨다.
    for start in product(points, repeat=2):
        # 해당 구역을 임시로 저장하는 배열.
        tmp_ice_map = [[0]*(2**fire_storm) for _ in range(2**fire_storm)]

        i_ = 0
        for i in range(start[0], start[0] + (2**fire_storm)):
            j_ = 0

            for j in range(start[1], start[1] + (2**fire_storm)):
                tmp_ice_map[i_][j_] = ice_map[i][j]
                j_ += 1

            i_ += 1

        # 임시로 저장한 배열을 90도 회전시킨다.
        i_ = start[0]
        for i in range(2**fire_storm):
            j_ = start[1]

            for j in range(2**fire_storm):
                # 90도 회전 시킨 배열을 원래의 맵에 저장한다.
                ice_map[i_][j_] = tmp_ice_map[2**fire_storm - j - 1][i]
                j_ += 1

            i_ += 1


def check_ice(ice_map, map_size):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    points = deque()

    for i in range(map_size):
        for j in range(map_size):
            ice_cnt = 0

            if ice_map[i][j] == 0:
                continue

            else:

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or ny < 0 or nx >= map_size or ny >= map_size or ice_map[nx][ny] == 0:
                        continue

                    ice_cnt += 1

                if ice_cnt < 3:
                    points.append([i, j])

    # 감소할 얼음의 위치를 찾아 뺀다.
    for p in points:
        x, y = map(int, p)
        ice_map[x][y] -= 1


def main():
    N, Q = map(int, input().split())

    map_size = 2**N
    ice_map = [[int(ice) for ice in input().split()] for _ in range(map_size)]

    fire_storms = [int(fire) for fire in input().split()]

    # 파이어 스톰 횟수만큼 진행한다.
    for fire_storm in fire_storms:
        # 구역을 나눈다.
        divide_and_turn_map(ice_map, fire_storm, map_size)

        # 구역이 3칸 미만인 곳을 체크한다.
        check_ice(ice_map, map_size)

    # 남아있는 얼음 수의 계산한다.
    sum_ice(ice_map, map_size)

    # 가장 큰 덩어리의 칸 수를 계산한다.
    find_big_ice(ice_map, map_size)


if __name__ == '__main__':
    main()
