# [아이디어]
# 영역의 개수를 찾기위해서 BFS를 이용해야한다.
# BFS 함수를 재사용하기 위해서 rg 값에 색약을 위한 값이면 True, 아니면 False를 넣어 이용한다.


from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

rg_cnt = 0
n_cnt = 0


def bfs(m, vi, status, i, j, rg, n):
    global n_cnt, rg_cnt, dx, dy

    q = deque()
    q.append([i, j])
    vi[i][j] = True

    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not vi[nx][ny] and m[nx][ny] == status:
                q.append([nx, ny])
                vi[nx][ny] = True

    if rg:
        rg_cnt += 1
    else:
        n_cnt += 1


def main():
    global n_cnt, rg_cnt

    n = int(input())
    m_n = [[0]*n for _ in range(n)]
    m_rg = [[0]*n for _ in range(n)]
    vi_n = [[False]*n for _ in range(n)]
    vi_rg = [[False]*n for _ in range(n)]

    for i in range(n):
        line = input()
        for j in range(n):
            m_n[i][j] = line[j]
            if line[j] == 'G':
                m_rg[i][j] = 'R'
            else:
                m_rg[i][j] = line[j]

    for i in range(n):
        for j in range(n):
            if not vi_n[i][j]:
                bfs(m_n, vi_n, m_n[i][j], i, j, False, n)
            if not vi_rg[i][j]:
                bfs(m_rg, vi_rg, m_rg[i][j], i, j, True, n)

    print(n_cnt, rg_cnt)


if __name__ == '__main__':
    main()
