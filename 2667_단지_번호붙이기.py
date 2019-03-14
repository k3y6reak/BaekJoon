# [아이디어]
# 입력 받은 맵에서 0인 부분은 미리 True로 표시한다. (방문을 안하기 위해서)
# 그러면 1인 부분만 방문을 하면 된다.
# 전체 배열을 탐색하면서 1인 부분만 들어간다. 해당 위치에서 델타배열을 이용해 주변의 방문할 수 있는 곳을 모두 방문하면서 개수를 센다.
# 개수를 하나의 배열에 넣어둔다.
# 그때 배열의 길이와 정렬된 값을 출력하면 된다.


from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

b = []


def bfs(m, vi, i, j, n):
    global b, dx, dy

    q = deque()
    q.append([i, j])
    vi[i][j] = True

    cnt = 1
    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not vi[nx][ny] and m[nx][ny] == '1':
                q.append([nx, ny])
                vi[nx][ny] = True
                cnt += 1

    b.append(cnt)


def main():
    global b

    n = int(input())
    m = [[0]*n for _ in range(n)]
    vi = [[False]*n for _ in range(n)]

    for i in range(n):
        line = input()
        for j in range(n):
            if line[j] == '0':
                vi[i][j] = True
            m[i][j] = line[j]

    b = []
    for i in range(n):
        for j in range(n):
            if m[i][j] == '1' and not vi[i][j]:
                bfs(m, vi, i, j, n)

    b.sort()
    print(len(b))
    for i in b:
        print(i)

if __name__ == '__main__':
    main()
