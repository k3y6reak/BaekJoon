# [아이디어]
# (1, 2) (2, 5) (5, 1) 이라면 1-2-5 의 연결관계를 갖는다.
# 이렇게 하나의 묶음으로 만들기위해서 disjoint set(서로소 집합)을 이용한다.
# union 함수를 이용해 각 번호들을 묶어준다.
# 1부터 n까지 돌면서 해당 값이 자기 부모랑 같으면 ans를 증가시켜준다.


parents = []
rank = []


def find_set(x):
    global parents, rank
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    global parents, rank
    px = find_set(x)
    py = find_set(y)

    if rank[px] > rank[py]:
        parents[py] = px
    else:
        parents[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


def make_set(x):
    global parents, rank

    parents[x] = x
    rank[x] = x


def main():
    global parents, rank

    n, m = map(int, input().split())

    parents = [0]*(n+1)
    rank = [0]*(n+1)

    for i in range(1, n + 1):
        make_set(i)

    for i in range(m):
        x, y = map(int, input().split())
        union(x, y)

    ans = 0
    for i in range(1, n + 1):
        if parents[i] == i:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
