def range_check(R, C, current_row, current_column):

    if R >= current_row or C >= current_column:
        return True

    return False


def extend_elements(elements):
    # 수는 100까지 존재한다. 숫자 카운팅용.
    cnt = [0] * 101

    for el in elements:
        cnt[el] += 1

    tmp = []
    for idx in range(1, 101):
        if cnt[idx] != 0:
            tmp.append((idx, cnt[idx]))

    # 정렬
    tmp = sorted(tmp, key=lambda x: (x[1], x[0]))

    sorted_tmp = []
    for t in tmp:
        sorted_tmp.append(t[0])
        sorted_tmp.append(t[1])

    # 크기가 100이 넘는 경우 100까지 자른다.
    if len(sorted_tmp) >= 100:
        return sorted_tmp[:100], 100

    return sorted_tmp, len(sorted_tmp)


def extend_map(map_, current_row, current_column):
    # 만약 R이 (행, 가로)가 C와 같거나 더 크면 행을 확장한다.(R연산)
    if current_row >= current_column:
        # 확장하면서 늘어나고, 줄어들 수 있다.
        max_column = 0

        # 현재 row의 값을 확장한다.
        for i in range(current_row):
            elements, column = extend_elements(map_[i])
            max_column = max(max_column, column)

            # 확장 한 후 해당 결과를 맵에 저장한다.
            for j in range(len(elements)):
                map_[i][j] = elements[j]

            # 확장한 경우에는 상관 없지만, 줄어든 경우에는 그 뒤 값을 초기화 시켜야 한다.
            for j in range(len(elements), 100):
                map_[i][j] = 0

        # 확장 시점에서의 최대 column을 저장한다.
        current_column = max_column

    # C가 더 크면 열을 확장한다.(C연산)
    else:
        max_row = 0

        for j in range(current_column):
            tmp_column = []
            for i in range(current_row):
                tmp_column.append(map_[i][j])

            elements, row = extend_elements(tmp_column)

            for i in range(len(elements)):
                map_[i][j] = elements[i]

            for i in range(len(elements), 100):
                map_[i][j] = 0

            max_row = max(max_row, row)

        current_row = max_row

    return map_, current_row, current_column


def main():
    R, C, K = map(int, input().split())
    R -= 1
    C -= 1

    # 100 * 100 배열을 만들어 놓는다.
    map_ = [[int(i) for i in input().split()] + ([0]*97) for _ in range(3)]

    for i in range(97):
        map_.append([0]*100)

    # 초기 row, column은 3.
    current_row = 3
    current_column = 3

    # 0-100까지 반복한다. range(100)으로 하면 74-5% 틀림.
    for t in range(101):

        # 만약, current_row, current_column 보다 R, C가 더 크면 범위 밖이다.
        if range_check(R, C, current_row, current_column):
            map_, current_row, current_column = extend_map(map_, current_row, current_column)

        # 범위 안이면.
        else:
            # R, C 위치의 값이 K와 같으면 시간을 출력하고 종료한다.
            if map_[R][C] == K:
                print(t)
                return

            # 다르면 확장을 진행한다.
            else:
                map_, current_row, current_column = extend_map(map_, current_row, current_column)

    print(-1)


if __name__ == '__main__':
    main()
