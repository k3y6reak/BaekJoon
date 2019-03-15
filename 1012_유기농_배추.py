# [아이디어]
# BFS 탐색을 통해서 1인 위치만 방문하여 델타배열을 이용해 탐색한다.
# 방문배열을 사용하지않기 위해서 1인 위치를 방문한 경우 x로 변경한다.


from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 0


def bfs(map_, i, j, m, n):
    global dx, dy, cnt

    q = deque()
    q.append([i, j])
    map_[i][j] = 'x'

    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if map_[nx][ny] == 1:
                q.append([nx, ny])
                map_[nx][ny] = 'x'

    cnt += 1


def main():
    global cnt

    for t in range(int(input())):
        m, n, k = map(int, input().split())
        map_ = [[0]*m for _ in range(n)]

        for i in range(k):
            y, x = map(int, input().split())
            map_[x][y] = 1

        cnt = 0
        for i in range(n):
            for j in range(m):
                if map_[i][j] == 1:
                    bfs(map_, i, j, m, n)

        print(cnt)


if __name__ == '__main__':
    main()
