# [아이디어]
# 플루이드-마샬 알고리즘을 이용해 각 사람별 촌수를 계산한다.


from math import inf

def main():
    n = int(input())
    s, e = map(int, input().split())
    m = int(input())
    map_ = [[inf]*n for _ in range(n)]

    for i in range(m):
        a, b = map(int, input().split())
        map_[a-1][b-1] = 1
        map_[b-1][a-1] = 1

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if map_[start][end] > map_[start][mid] + map_[mid][end]:
                    map_[start][end] = map_[start][mid] + map_[mid][end]

    tmp = map_[s-1][e-1]
    if tmp == inf:
        print(-1)
    else:
        print(tmp)


if __name__ == '__main__':
    main()
