# [아이디어]
# 집을 저장할 큐를 만들고 x, y, 치킨집과의 최소거리를 넣는다.
# 치킨집을 저장할 큐를 만들고 x, y를 넣는다.
# 최소 1개, 최대 M개의 집을 선택할 수 있으므로 전체 치킨집에 대해서 0은 선택안함, 1은 선택함으로 구분하여 중복순열을 만들어낸다.
# 중복순열을 만들때 1의 개수가 최소 1개 최대 M개가 되는 것만 구성한다.
# 해당 치킨집이 1일때 살아남은 치킨집이므로 해당 치킨집부터 전체 집의 거리를 계산하여 최솟값을 저장한다.
# 다른 치킨집이 1일때 마찬가지로 모든 집과의 거리를 계산하여 최솟값을 저장한다.
# 최솟값이 계산된 집들의 거리를 더해 가장 작은 거리가 되는 값을 찾는다.

import collections
import itertools

low = 99999

def search(homes, chickens, pick, chickens_cnt, homes_cnt):
    global low

    # 치킨집의 개수만큼 돌면서 pick의 값이 1인 집만 선택하여 집의 좌표들과 거리를 계산한다.
    # 계산한 거리가 현재 거리보다 작으면 넣는다.
    for i in range(chickens_cnt):
        if pick[i] == 1: # 선택된 치킨집이면,
            # 치킨집의 좌표를 가져온다.
            chicken = chickens[i]
            c_x = chicken[0]
            c_y = chicken[1]

            # 집들을 전부탐색하여
            for home in homes:
                h_x = home[0]
                h_y = home[1]

                # 해당 치킨집과 거리를 계산하여 현재거리와 비교하여 작은 값을 넣는다.
                interval = abs(c_x - h_x) + abs(c_y - h_y)
                home[2] = min(home[2], interval)


    # 집들의 거리가 모두 계산되면 그 합을 계산하여 최소값을 저장한다.
    low_interval = 0
    for i in range(homes_cnt):
        low_interval += homes[i][2]

    low = min(low, low_interval)


def set_homes(homes, home_cnt):
    tmp = collections.deque()
    for i in range(home_cnt):
        x = homes[i][0]
        y = homes[i][1]
        interval = 99999
        tmp.append([x, y, interval])

    return tmp


def main():
    global low

    N, M = map(int, input().split())
    map_ = [[0]*N for _ in range(N)]

    homes = collections.deque()
    chickens = collections.deque()

    # 집들은 좌표와 치킨집과의 최소거리를 저장할 배열을 큐에 넣는다.
    # 치킨집은 좌표를 큐에 넣는다.
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            tmp = line[j]
            if tmp == 1:
                homes.append([i, j, 99999])
            elif tmp == 2:
                chickens.append([i, j])
            map_[i][j] = tmp

    # M이 선택할 수 있는 최대의 치킨집 개수이다.
    # 중복순열을 이용해 0이면 선택안함, 1이면 선택함을 만들어낸다.
    # 이때 1의 개수가 M보다 작은 경우와 최소 1개일때만 진행한다.
    chickens_cnt = len(chickens)
    homes_cnt = len(homes)
    low = 99999
    for i in itertools.product(range(2), repeat=chickens_cnt):
        one_cnt = i.count(1)
        if one_cnt != 0 and one_cnt <= M:
            search(set_homes(homes, homes_cnt), chickens, i, chickens_cnt, homes_cnt)

    print(low)


if __name__ == '__main__':
    main()
