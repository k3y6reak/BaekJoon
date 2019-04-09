# [아이디어]
# 한번 탐색시 맵 전체를 탐색한다.
# 전체 탐색시 해당 좌표부터 연합이 구성될 수 있는 좌표들을 큐에 넣는다. 연합 큐에도 함께 넣는다.
# 큐가 비어버리면 해당 연합 구성이 끝난 것으로 연합 구성시 길이가 1이면 자기 자신만 연합이므로 제외한다.
# 연합 길이가 2이상이되면 연합을 구성할 수 있기 때문에 연합 큐에서 하나씩 빼서 평균 값을 넣어준다.
# 큐가 다 비었으면 연합 번호를 증가시켜 다른 연합임을 표시한다.
# vi 배열이 모두 0이면 더이상 연합을 구성할 수 없으므로 False를 리턴하여 종료한다.
# 연합을 구성할 수 있는 상태라면 True를 반환하고 횟수를 증가시킨다.


import collections

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def search(map_, vi, N, L, R):

    q = collections.deque()
    idx = 1 # 각 idx 별 연합을 구성하기 위한 변수

    # 전체 맵을 탐색해서 해당 좌표에서 연합이 될 수 있는 곳을 찾자.
    for i in range(N):
        for j in range(N):
            # 해당 좌표가 방문하지 않은 곳일때
            yeonhap = collections.deque()
            if vi[i][j] == 0:
                yeonhap.append([i, j])
                q.append([i, j]) # 해당 좌표를 큐에 넣는다.
                vi[i][j] = idx
                # 큐가 비어있지 않는 동안
                while q:
                    p = q.popleft()
                    x = p[0]
                    y = p[1]

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        # 범위 밖이면 버림.
                        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                            continue

                        # 연합이 될 수 있는 것이면서 연합이 구성되지 않는 것만.
                        if vi[nx][ny] == 0 and L <= abs(map_[x][y] - map_[nx][ny]) <= R:
                            # 연합번호를 부여한다.
                            vi[nx][ny] = idx
                            q.append([nx, ny])
                            yeonhap.append([nx, ny])

                # 전부 돌았음에도 하나만 연합이면
                if len(yeonhap) == 1:
                    p = yeonhap.popleft()
                    vi[p[0]][p[1]] = 0

                elif len(yeonhap) > 1:
                    yeonhap_cnt = len(yeonhap)
                    yeonhap_sum = 0
                    # 연합들의 큐를 돌아 값을 가져옴.
                    for y in range(yeonhap_cnt):
                        y_tmp = yeonhap[y]
                        yeonhap_sum += map_[y_tmp[0]][y_tmp[1]]

                    yeonhap_avg = yeonhap_sum // yeonhap_cnt
                    while yeonhap:
                        y_tmp = yeonhap.popleft()
                        map_[y_tmp[0]][y_tmp[1]] = yeonhap_avg

                # 큐가 다 비었으면, 연합 번호를 증가시킨다.
                idx += 1

    # 맵을 전체 탐색했다면 vi가 연합별로 설정이 되있을 것이다.
    # 만약 연합이 구성되지 않으면 vi는 모두 0으로 설정.
    # 모두 0이면 더 이상 탐색을 하지 않는다.
    end_flag = False
    for i in range(N):
        for j in range(N):
            if vi[i][j] != 0:
                end_flag = True
                break
        if end_flag:
            break

    return end_flag


def main():
    N, L, R = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(N)]

    search_cnt = 0
    flag = True
    while flag:
        vi = [[0]*N for _ in range(N)]
        flag = search(map_, vi, N, L, R)
        if flag:
            search_cnt += 1

    print(search_cnt)



if __name__ == '__main__':
    main()
