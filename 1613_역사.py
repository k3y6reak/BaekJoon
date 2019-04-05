# [아이디어]
# 플루이드-마샬 알고리즘을 이용한다.
# 역사의 순서에 따라, 1과 -1로 구분한다.
# A에서 B로 발생하 사건이면 1, B에서 A로 발생한 사건이면 -1을 준다.
# 탐색하면서 A에서 C, C에서 B로 발생한 사건이면 A에서 B로 발생한 사건과 같다.

from math import inf

def main():
    n, k = map(int, input().split())
    map_ = [[inf]*n for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        map_[a-1][b-1] = -1
        map_[b-1][a-1] = 1

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                # 시작점부터 중간점 순으로 발생하고, 중간점부터 끝 점으로 발생한 사건이라면.
                if map_[start][mid] == 1 and map_[mid][end] == 1:
                    map_[start][end] = 1 # 시작점과 끝점 순으로 발생한것
                    map_[end][start] = -1

                elif map_[start][mid] == -1 and map_[mid][end] == -1:
                    map_[start][end] = -1
                    map_[end][start] = 1

    s = int(input())

    for i in range(s):
        a, b = map(int, input().split())
        if map_[a-1][b-1] == inf:
            print(0)
        else:
            print(map_[a-1][b-1])


if __name__ == '__main__':
    main()
