from collections import deque


class Shark:
    def __init__(self, x, y, size, eat_cnt, move_cnt):
        self.x = x
        self.y = y
        self.size = size
        self.eat_cnt = eat_cnt
        self.move_cnt = move_cnt


class Fish:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_shark(map_, shark, N):

    visited = [[False]*N for _ in range(N)]

    q = deque()
    q.append([shark.x, shark.y, 0])
    visited[shark.x][shark.y] = True
    possible_eat = []

    while len(q) != 0:
        el = q.popleft()

        x = el[0]
        y = el[1]
        move_cnt = el[2]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖, 방문, 물고기의 크기가 크면 이동할 수 없다.
            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] or (map_[nx][ny] != 0 and map_[nx][ny].size > shark.size):
                continue

            # 이동한 위치를 체크
            visited[nx][ny] = True
            q.append([nx, ny, move_cnt + 1])

            # 상어의 위치가 아니면서, 물고기이면서 상어보다 크기가 작은 경우는 먹을 수 있다.
            if not (nx == shark.x and ny == shark.y) and map_[nx][ny] != 0 and map_[nx][ny].size < shark.size:
                possible_eat.append([nx, ny, move_cnt + 1, map_[nx][ny].size])

    # 먹을 수 있는 물고기들 중, 가장 가까우면서, 가장 위에 있고, 가장 왼쪽에 있는 것으로 정렬한다.
    possible_eat = sorted(possible_eat, key=lambda x: (x[2], x[0], x[1]))

    # 먹을 수 있는 물고기가 있으면,
    if possible_eat:
        x, y, move_cnt, size = map(int, possible_eat[0])

        # 물고기의 크기가 상어의 크기보다 작은 경우만,
        if size < shark.size:
            map_[x][y] = 0
            shark.move_cnt += move_cnt
            shark.eat_cnt += 1

            # 물고기를 먹은 후, 상어의 크기와 같으면 크기를 증가시킨다.
            if shark.eat_cnt == shark.size:
                shark.size += 1
                shark.eat_cnt = 0

            shark.x = x
            shark.y = y
        else:
            return map_, shark, shark.move_cnt, False

        return map_, shark, shark.move_cnt, True
    else:
        return map_, shark, shark.move_cnt, False


def main():
    N = int(input())

    # 맵 세팅 및 상어 정보 저장.
    map_ = [[0]*N for _ in range(N)]
    shark_xy = [0, 0]
    for i in range(N):
        for j, tmp in enumerate(input().split()):
            if int(tmp) == 9:
                shark_xy[0] = i
                shark_xy[1] = j
            elif int(tmp) != 0:
                map_[i][j] = Fish(i, j, int(tmp))

    flag = True
    shark = Shark(shark_xy[0], shark_xy[1], 2, 0, 0)
    while flag:
        # 상어를 이동시킨다.
        map_, shark, move_cnt, flag = move_shark(map_, shark, N)

        # 더 이상 이동할 수 없으면 이동 시간을 출력한다.
        if not flag:
            print(move_cnt)


if __name__ == '__main__':
    main()
