# [아이디어]
# 배열 하나를 검색할 수 있는 함수를 만들어 진행한다.
# 이때 배열을 체크할때 높이가 같은 경우와 다른 경우로 분류한다.
# 높이가 다른 경우에는 그 차이가 1인지 확인하고 1인 경우에만 수행한다.
# 차이가 1일때, 경사로를 놓을 수 있는지 확인해야 한다.
# 경사로를 놓을때 이미 놓아져있거나, 경사로의 길이보다 작으면 놓을 수 없다.
# 경사로의 길이보다 맵의 길이가 작은지를 잘 체크해야 한다.
# 경사로를 놓을 수 있다면 vi 배열에 해당 위치에 True로 변경하여 놓았다는 표시를 한다.

def check(root, N, L):
    # 처음 위치부터 하나씩 이동
    # 이동할때 다음 값이 같으면 그냥 이동
    # 작거나 큰 경우 => 차이가 1이어야 함.

    vi = [False]*N

    for i in range(N - 1):
        if root[i] == root[i + 1]: # 높이가 같은 경우는 지나간다.
            continue

        elif root[i] != root[i + 1]: # 높이가 다른 경우.
            if abs(root[i] - root[i + 1]) != 1: # 높이의 차가 1이 아닌 경우는 경사로를 놓아도 갈 수 없음.
                return "no"
            else:
                # 높이의 차가 1이면서 높은 경우
                if root[i + 1] - root[i] == 1:
                    # 현재 위치에서 길이 보다 작으면 놓을 수 없음.
                    if i - L < -1:
                        return "no"

                    # 현재 위치 i 부터 L 만큼 뒤를 보고
                    for j in range(i, i - L, -1):
                        if root[i] != root[j] or vi[j]: # 현재 위치부터 뒤로 길이만큼가면서 다르면 경사로를 놓을 수 없음.
                            return "no"         # 또는 해당 위치에 경사로를 놓았다면 놓을 수 없음.

                    # 뒤를 확인 했는데, 놓을 수 있다면
                    for j in range(i, i - L, -1):
                        vi[j] = True

                # 높이의 차가 1이면서 낮은 경우
                elif root[i] - root[i + 1] == 1:
                    # 현재 위치에서 길이 보다 작으면 놓을 수 없음
                    if i + L >= N:
                        return "no"

                    # 다음 위치 i+1 부터 L 만큼 앞을 보고
                    for j in range(i + 1, i + L + 1):
                        if root[i+1] != root[j]:
                            return "no"

                    for j in range(i + 1, i + L + 1):
                        vi[j] = True

    return "ok"

def main():
    N, L = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 가로 탐색
    for i in range(N):
        root = map_[i]
        res = check(root, N, L)

        if res == "no":
            res = check(root[::-1], N, L)

        if res == "ok":
            cnt += 1

    # 세로 탐색
    for j in range(N):
        root = []
        for i in range(N):
            root.append(map_[i][j])

        res = check(root, N, L)
        if res == "no":
            res = check(root[::-1], N, L)

        if res == "ok":
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
