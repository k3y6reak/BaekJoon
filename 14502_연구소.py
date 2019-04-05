# [아이디어]
# 총 3개의 벽을 세워야한다. 사람의 눈으로는 어디에 두어야 할지 알지만, 코드로 작성을해야하기 때문에 3개의 점을 뽑도록 조합을 구성한다.
# 사람의 관점으로 접근하면 탐욕적으로 접근하기 때문에 실패할 확률이 크다.!!
# 3개의 점을 뽑아 미리 2가 있는 바이러스를 리스트에 담아두고 이를 check함수에서 큐에 넣어둔다.
# 그 후 BFS 탐색으로 바이러스를 퍼트리고 안전영역의 수를 센다
# 다음 점도 확인하기 위해서 맵과 방문 배열을 초기화한다.

from collections import deque
from itertools import combinations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

big = 0

def check(map_, vi, point, virus, N, M):
    global big, dx, dy

    for p in point:
        map_[p[0]][p[1]] = 1

    q = deque()

    for v in virus:
        q.append([v[0], v[1]])
        vi[v[0]][v[1]] = True

    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if (not vi[nx][ny]) and map_[nx][ny] == 0:
                vi[nx][ny] = True
                map_[nx][ny] = 2
                q.append([nx, ny])

    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_[i][j] == 0:
                cnt += 1

    big = max(big, cnt)



def set_map(map_, N, M):
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = map_[i][j]

    return tmp

def main():
    global big

    N, M = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(N)]

    points = deque()
    virus = deque()
    for i in range(N):
        for j in range(M):
            if map_[i][j] == 0:
                points.append([i, j])
            elif map_[i][j] == 2:
                virus.append([i, j])
    big = 0
    for point in combinations(points, 3):
        vi = [[0]*M for _ in range(N)]
        check(set_map(map_, N, M), vi, point, virus, N, M)

    print(big)


if __name__ == '__main__':
    main()
