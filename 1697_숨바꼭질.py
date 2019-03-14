# [아이디어]
# 시작 지점부터 끝 지점까지 -1, +1, *2 씩 이동할수 있다.
# 이동할수 있는 값을 큐에 넣고 탐색한다. BFS
# 중요!! python에서 import queue 보다 collections.deque가 더 빠르다.
# 리스트를 큐로 사용하면 시간 복잡도가 크다.

from collections import deque


def bfs(start, end, vi):
    q = deque()
    q.append([start, 0])
    vi[start] = True

    while q:
        p = q.popleft()

        if p[0] < 0 or p[0] > 100000:
            continue

        if p[0] == end:
            return p[1]

        if p[0] + 1 <= 100000 and not vi[p[0] + 1]:
            q.append([p[0] + 1, p[1] + 1])
            vi[p[0] + 1] = True

        if p[0] - 1 >= 0 and not vi[p[0] - 1]:
            q.append([p[0] - 1, p[1] + 1])
            vi[p[0] - 1] = True

        if p[0] * 2 <= 100000 and not vi[p[0] * 2]:
            q.append([p[0] * 2, p[1] + 1])
            vi[p[0] * 2] = True


def main():
    start, end = map(int, input().split())
    vi = [False]*100001

    print(bfs(start, end, vi))


if __name__ == '__main__':
    main()
