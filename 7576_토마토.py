# [아이디어]
# 맵 정보를 입력받으면서 토마토(1)를 바로 큐에 넣어준다.
# BFS 탐색을 하면서 큐에서 하나씩 가져와 다음 이동위치가 0인 경우에 큐에 넣어준다.
# 여기서 방문배열을 사용하지 않은 이유는 맵 자체에 해당 시간을 표시하면 된다.
# 맵을 탐색하면서 0이 있으면 바로 -1을 출력하고 return 하고, 아닌 경우에는 가장 큰 값을 찾아 출력한다.
# 이때 가장 큰 값에 -1을 하면 답이된다.

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()


def bfs(map_, m, n):
    global q, dx, dy

    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if map_[nx][ny] == 0:
                q.append([nx, ny, p[2] + 1])
                map_[nx][ny] = p[2] + 1


    big = 0
    for i in range(n):
        for j in range(m):
            if map_[i][j] == 0:
                print(-1)
                return
            else:
                if map_[i][j] > big:
                    big = map_[i][j]

    print(big-1)

def main():
    global q

    m, n = map(int, input().split())
    map_ = [[0]*m for _ in range(n)]

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j] == 1:
                q.append([i, j, 1])
            map_[i][j] = line[j]

    bfs(map_, m, n)




if __name__ == '__main__':
    main()
