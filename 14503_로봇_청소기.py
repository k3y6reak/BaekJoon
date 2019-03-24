# [아이디어]
# DFS 탐색을 진행한다.
# 사방탐색을 통해 청소가 가능하다면, 방향을 기준으로 왼쪽방향으로 이동한다.
# 이동한 구역이 벽인 경우에는 바로 종료시킨다.
# 청소할 구역도 없고, 뒤로도 갈 수 없는 경우 끝낸다.



cnt = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

search_flag = False
back_flag = False
end_flag = False


def dfs(map_, i, j, a, n, m):
    global cnt, search_flag, back_flag, end_flag

    back_flag = False

    if map_[i][j] == 1:
        end_flag = True

    if end_flag:
        return

    for q in range(4): # 해당 위치에서 사방탐색을 진행하고, 주위에 청소할 수 있다면
        x = i + dx[q]
        y = j + dy[q]

        if x < 0 or y < 0 or x >= n or y >= m:
            continue

        if map_[x][y] == 0: # search_flag를 true로 변경한다.
            search_flag = True
            break

    if not search_flag and back_flag: # 청소할 수 없거나, 뒤로도 갈 수 없는 경우, 끝낸다.
        end_flag = True
        return

    if not search_flag: # 사방탐색 후 청소할 구역이 없다면 해당 방향에서 뒤로 진행한다.
        if a == 0 and i + 1 < n: # 북쪽
            search_flag = False
            back_flag = True
            dfs(map_, i + 1, j, a, n, m)

        elif a == 1 and j - 1 >= 0: # 동쪽
            search_flag = False
            back_flag = True
            dfs(map_, i, j - 1, a, n, m)

        elif a == 2 and i - 1 >= 0: # 남쪽
            search_flag = False
            back_flag = True
            dfs(map_, i - 1, j, a, n, m)

        elif a == 3 and j + 1 < m: # 서쪽
            search_flag = False
            back_flag = True
            dfs(map_, i, j + 1, a, n, m)

    else: # 청소할 구역이 있다면.
        if a == 0: # 북쪽
            back_flag = False
            if j - 1 >= 0 and map_[i][j - 1] == 0: # 서쪽을 바라보고 이동한다.
                j -= 1
                search_flag = False
                map_[i][j] = 'x'
                cnt += 1
                dfs(map_, i, j, 3, n, m)
            else:
                dfs(map_, i, j, 3, n, m)

        elif a == 1: # 동쪽
            back_flag = False
            if i - 1 >= 0 and map_[i - 1][j] == 0:# 북쪽을 바라보고 이동한다.
                i -= 1
                search_flag = False
                map_[i][j] = 'x'
                cnt += 1
                dfs(map_, i, j, 0, n, m)
            else: # 이미 청소한 구역이면 방향을 바꾼다.
                dfs(map_, i, j, 0, n, m)

        elif a == 2: # 남쪽
            back_flag = False
            if j + 1 < m and map_[i][j + 1] == 0: # 동쪽을 바라보고 이동한다.
                j += 1
                search_flag = False
                map_[i][j] = 'x'
                cnt += 1
                dfs(map_, i, j, 1, n, m)
            else:
                dfs(map_, i, j, 1, n, m)

        elif a == 3: # 서쪽
            back_flag = False
            if i + 1 < n and map_[i + 1][j] == 0: # 남쪽을 바라보고 이동한다.
                i += 1
                map_[i][j] = 'x'
                cnt += 1
                search_flag = False
                dfs(map_, i, j, 2, n, m)
            else:
                dfs(map_, i, j, 2, n, m)


def main():
    global cnt

    n, m = map(int, input().split())
    x, y, a = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(n)]

    map_[x][y] = 'x'
    cnt += 1

    dfs(map_, x, y, a, n, m)
    print(cnt)


if __name__ == '__main__':
    main()
