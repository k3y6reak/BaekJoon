# [아이디어]
# DP로 접근한다.
# 이전의 값에서 점차 더하면서 큰 값을 가져와야 하므로 만들 배열보다 1칸 더 크게 만들어야 한다.
# 인덱스의 범위를 조심하여 계산하면된다.
#
# 7                                           0 0 0 0 0
# 3 8                                         7 0 0 0 0
# 8 1 0       왼쪽과 같이 입력이 들어온다면     3 8 0 0 0  와 같이 리스트에 저장한다.
# 2 7 4 4                                     8 1 0 0 0
# 4 5 2 6 5                                   2 7 4 4 0
#                                             4 5 2 6 5
#
#  7 0 0 0 0 은 이전의 값 0 0 0 0 0 에서 7의 위치의 바로 윗칸과 윗칸 왼쪽이 대각선이 된다. 범위 밖이면 바로 위만 계산한다.




def main():
    n = int(input())
    map_ = [[0]*n]

    for i in range(n):
        line = list(map(int, input().split()))
        tmp = []
        if len(line) <= n:
            t = n - len(line)
            tmp = [0]*t
        map_.append(line + tmp)

    for i in range(1, n+1):
        for j in range(n):
            if j - 1 < 0:
                map_[i][j] += map_[i-1][j]
            else:
                map_[i][j] += max(map_[i-1][j], map_[i-1][j-1])

    print(max(map_[-1]))


if __name__ == '__main__':
    main()
