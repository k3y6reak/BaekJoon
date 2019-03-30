# [아이디어]
# 처음 특정점을 기준으로 나머지 점들을 세대마다 돌려 커브가 만들어지는 점을 확인하려했으나, 회전시킬 방법이 떠오르지 않았다.
# 현재까지 진행된 방향을 기준으로 거꾸로 방향을 보면서 다음 방향을 찾아내고, 해당 방향으로 점을 이동시키면 된다.
# 오른쪽 방향이면 다음 방향은 위쪽이 된다.
# 위쪽 방향이면 다음 방향은 왼쪽이 된다.
# 왼쪽 방향이면 아래 방향이 된ㄷ.
# 이러한 규칙을 찾아 찾아갈 다음 방향들을 계속해 넣어준다.
# 그 방향대로 이동한 점을 True로 변경하여 모든 점들을 탐색해 각 꼭짓점이 True인 것을 카운팅한다.



     #>  ^  <   v
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
end_x = 0
end_y = 0
map_ = []


def dragon(go):
    global end_x, end_y, dx, dy, map_

    go_len = len(go)

    # 방향정보 리스트를 거꾸로 탐색하면서 해당 방향의 다음 방향을 결정한다.
    for i in range(go_len-1, -1, -1):
        goto = (go[i] + 1) % 4
        end_x = end_x + dx[goto]
        end_y = end_y + dy[goto]

        map_[end_x][end_y] = True

        go.append(goto)


def main():
    global dx, dy, end_x, end_y, map_

    map_ = [[0]*102 for _ in range(102)]

    for n in range(int(input())):
        y, x, d, g = map(int, input().split())

        # 처음 입력받은 점을 True로 설정
        map_[x][y] = True

        # 0세대 점도 True로 설정
        end_x = x + dx[d]
        end_y = y + dy[d]
        map_[end_x][end_y] = True
        go = []
        # 현재 방향을 리스트에 저장.
        go.append(d)

        # g 세대까지 만들자.
        for i in range(g):
            dragon(go)

    cnt = 0
    for i in range(101):
        for j in range(101):
            if map_[i][j] and map_[i][j+1] and map_[i+1][j] and map_[i+1][j+1]:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
