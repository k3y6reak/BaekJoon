from itertools import combinations
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def virus_check(map_, N, active_virus):
    for i in range(N):
        for j in range(N):
            if map_[i][j] == 0 and [i, j] not in active_virus:
                return False

    return True


def move_virus(possible_virus_xy, map_, N):

    # 바이러스가 퍼지는 최대 시간.
    max_time = 0

    # 현재 놓을 수 있는 바이러스의 위치를 큐에 넣어준다.
    q = deque()

    visited = [[False] * N for _ in range(N)]

    for virus in possible_virus_xy:
        q.append(virus + [0])
        visited[virus[0]][virus[1]] = True

    # 큐에서 하나씩 꺼내서 상, 하, 좌, 우 이동한다.
    while len(q) != 0:

        el = q.popleft()

        x = el[0]
        y = el[1]
        time = el[2]

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖으로 이동할 수 없다.
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 비활성 바이러스이면서, 그 위치를 방문하지 않은 경우.
            if map_[nx][ny] == "*" and not visited[nx][ny]:
                # 다음 이동이 있을 수 있으니 시간을 증가 시켜 큐에 넣어준다.
                q.append([nx, ny, time + 1, True])
                visited[nx][ny] = True
                continue

            # 벽이면 이동할 수 없다.
            if map_[nx][ny] == "-":
                continue

            # 이미 바이러스가 퍼져있는데, 그 시간이 기록할 시간보다 작으면 이동 할 필요 없음.
            if map_[nx][ny] != 0 and map_[nx][ny] != "*" and map_[nx][ny] <= time:
                continue

            # 비어있는 공간이고, 방문할 수 있으면
            if map_[nx][ny] == 0 and not visited[nx][ny]:
                # 해당 위치에 시간을 기록한다.
                map_[nx][ny] = time + 1
                visited[nx][ny] = True
                q.append([nx, ny, time + 1])
                max_time = max(max_time, time + 1)

    flag = virus_check(map_, N, possible_virus_xy)

    if flag:
        return max_time
    else:
        return -1


def init_map(map_, N, not_active_virus):
    tmp_map = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            tmp_map[i][j] = map_[i][j]

    for virus in not_active_virus:
        x, y = map(int, virus)
        tmp_map[x][y] = "*"

    return tmp_map


def main():
    N, M = map(int, input().split())

    map_ = []
    virus_xy = []
    min_time = 99999
    zero_area = 0

    for i in range(N):
        tmp = []
        for idx, j in enumerate(input().split()):
            if int(j) == 1:
                tmp.append("-")
                continue
            elif int(j) == 2:
                virus_xy.append([i, idx])
                tmp.append(0)
                zero_area += 1
            else:
                tmp.append(int(j))

        map_.append(tmp)

    # 바이러스가 움직일 공간이 없으면 0초.
    if zero_area == 0:
        print(0)
        return 0

    # 바이러스를 놓은 위치를 조합으로 선정.
    for possible_virus_xy in combinations(virus_xy, M):
        not_active_virus = []

        for virus in virus_xy:
            if virus not in possible_virus_xy:
                not_active_virus.append(virus)

        # 맵 초기화 후, 이동.
        time = move_virus(possible_virus_xy, init_map(map_, N, not_active_virus), N)

        # 시간이 -1인 경우를 제외하고, 최소 시간을 찾는다.
        if time != -1:
            if time == 0: # 시간이 0이면 그 보다 빠를 수 없다.
                print(0)
                return

            # 최소 시간을 갱신한다.
            min_time = min(min_time, time)

    # 어떻게 놓아도 바이러스를 모두 이동시킬 수 없다면 -1
    if min_time == 99999:
        print(-1)
    else:
        print(min_time)


if __name__ == '__main__':
    main()
