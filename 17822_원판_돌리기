from collections import deque


def turn_circle(circle, X, D, K):
    """
    :param circle: 변경 전 원판
    :param X: X 배수 원판 선택
    :param D: 방향 (0: 시계방향, 1: 반시계방향)
    :param K: 회전 횟수
    :return: 변경된 원판
    """

    # 원판을 하나 꺼내온다.
    for idx in range(len(circle)):
        if (idx + 1) % X == 0:
            if D == 0:
                circle[idx].rotate(K)
            elif D == 1:
                circle[idx].rotate(-K)

    return circle


def remove_circle(circle, N, M):
    """

    :param circle: 삭제전 원판
    :param N: 원판 개수 (x)
    :param M: 한 원판의 숫자 개수 (y)
    :return: 삭제된 원판, 삭제 여부
    """

    # 델타 배열
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 방문 배열을 만든다.
    visited = deque()
    for n in range(N):
        visited.append([False] * M)

    # 삭제 여부 판단
    delete_flag = False

    for n in range(N):
        for m in range(M):
            # 현재 방문하고자 하는 곳이 방문하지 않았거나, 삭제가 되지 않는 경우만 진입.
            if not visited[n][m] and circle[n][m] != "x":
                q = deque()
                q.append([n, m, circle[n][m]])

                while len(q) != 0:
                    el = q.pop()
                    x = el[0]
                    y = el[1]
                    value = el[2]

                    # 상, 하, 좌, 우 탐색.
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        # 배열의 첫번째 요소에서 델타배열 이동 시, y축 값이 -1이 되면 원판의 끝 위치.
                        # 첫번재 요소와 끝 요소가 같은지 확인해야하며, 같으면 큐에 넣는다.
                        if 0 <= nx < N and ny == -1 and circle[nx][M-1] != "x" and (not visited[nx][M-1]):
                            if circle[x][y] == circle[nx][M-1]:
                                visited[x][y] = True
                                visited[nx][M-1] = True
                                q.append([nx, M-1, circle[nx][M-1]])
                                continue

                        # 배열의 마지막 요소에서 델타배열 이동 시, y축 값이 M이 되면 원판의 첫 위치.
                        # 마지막 요소와 첫 요소가 같은지 확인해야하며, 같으면 큐에 넣는다.
                        if 0 <= nx < N and ny == M and circle[nx][0] != "x" and (not visited[nx][0]):
                            if circle[x][y] == circle[nx][0]:
                                visited[x][y] = True
                                visited[nx][0] = True
                                q.append([nx, 0, circle[nx][0]])
                                continue

                        if nx < 0 or ny < 0 or nx >= N or ny >= M:
                            continue

                        # 첫, 끝 요소의 조건이 아닌 경우, 탐색.
                        if (not visited[nx][ny]) and circle[nx][ny] != "x" and circle[nx][ny] == value:
                            visited[x][y] = True
                            visited[nx][ny] = True
                            q.append([nx, ny, circle[nx][ny]])

    # 탐색 시 방문한 경우라면, 같은 값이 있다는 의미.
    for n in range(N):
        for m in range(M):
            if visited[n][m]:
                delete_flag = True
                circle[n][m] = "x"

    return circle, delete_flag


def calc_circle(circle, N, M):
    """

    :param circle: 원판
    :param N: 원판 갯수
    :param M: 한 원판의 숫자 갯수
    :return: 평균이 계산된 원판
    """
    sum_elements = 0.0
    cnt = 0

    for n in range(N):
        for m in range(M):
            if circle[n][m] != "x":
                sum_elements += circle[n][m]
                cnt += 1

    if cnt != 0 or sum_elements != 0:
        avg = sum_elements / cnt

        for n in range(N):
            for m in range(M):
                if circle[n][m] != "x":
                    if circle[n][m] < avg:
                        circle[n][m] += 1
                    elif circle[n][m] > avg:
                        circle[n][m] -= 1

    return circle


def sum_circle(circle, N, M):
    sum_elements = 0

    for n in range(N):
        for m in range(M):
            if circle[n][m] != "x":
                sum_elements += circle[n][m]

    return sum_elements


def main():
    # N: 원판 갯수
    # M: 한 원판의 숫자 개수
    # T: 회전 횟수
    N, M, T = map(int, input().split())

    circle = deque()
    for n in range(N):
        circle.append(deque(map(int, input().split())))

    for t in range(T):
        # X: 배수
        # D: 방향
        # K: 이동 횟수
        X, D, K = map(int, input().split())

        # 원판을 회전시킨다.
        circle = turn_circle(circle, X, D, K)

        # 같은 숫자를 삭제한다.
        circle, delete_flag = remove_circle(circle, N, M)

        # 만약, 삭제된 숫자가 없다면,
        if not delete_flag:
            # 원판의 평균을 구해 계산한다.
            circle = calc_circle(circle, N, M)

    # 원판의 합을 구한다.
    print(sum_circle(circle, N, M))


if __name__ == '__main__':
    main()
