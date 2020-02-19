UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4


class Shark:
    def __init__(self, x, y, speed, arrow, size, move_flag):
        self.x = x
        self.y = y
        self.speed = speed
        self.arrow = arrow
        self.size = size
        self.move_flag = move_flag


def remove_shark(map_, shark_list, idx, R):
    # 상거가 잡혔거나, 다른 상어에게 먹힌 경우 제거하는 함수.
    for i in range(R):
        if map_[i][idx] != 0:
            catch_shark = map_[i][idx]
            shark_list.remove(catch_shark)
            map_[i][idx] = 0
            return map_, shark_list, catch_shark.size

    return map_, shark_list, 0


def move_shark(map_, shark_list, R, C):
    eat_shark_list = []

    for shark in shark_list:
        # 모두 한 칸에 존재하니 이동하기 전에 위치를 0으로 해도 상관 없음.
        # 이미 이동해서 해당 위치에 존재하는 상어는 없애면 안됨.
        if not map_[shark.x][shark.y].move_flag:
            map_[shark.x][shark.y] = 0

        tmp_x = shark.x
        tmp_y = shark.y

        remain_move = shark.speed
        while remain_move != 0:
            arrow = shark.arrow

            if arrow == UP:
                if min(remain_move, tmp_x) == tmp_x:
                    remain_move -= tmp_x
                    tmp_x = 0
                    shark.arrow = DOWN
                else:
                    tmp_x = tmp_x - remain_move
                    remain_move = 0

            elif arrow == DOWN:
                if min(remain_move, R - tmp_x) == R - tmp_x:
                    remain_move -= (R - tmp_x - 1)
                    tmp_x = R - 1
                    shark.arrow = UP
                else:
                    tmp_x = tmp_x + remain_move
                    remain_move = 0

            elif arrow == RIGHT:
                if min(remain_move, C - tmp_y - 1) == C - tmp_y - 1:
                    remain_move -= (C - tmp_y - 1)
                    tmp_y = C - 1
                    shark.arrow = LEFT
                else:
                    tmp_y = tmp_y + remain_move
                    remain_move = 0

            elif arrow == LEFT:
                if min(remain_move, tmp_y) == tmp_y:
                    remain_move -= tmp_y
                    tmp_y = 0
                    shark.arrow = RIGHT
                else:
                    tmp_y = tmp_y - remain_move
                    remain_move = 0

        # 이동이 완료된 위치에 상어가 존재하고, 이동이 완료된 상어라면,
        if map_[tmp_x][tmp_y] != 0 and map_[tmp_x][tmp_y].move_flag:
            tmp_shark = map_[tmp_x][tmp_y]

            # 이미 존재한 상어의 크기보다 현재 상어가 더 크면,
            if tmp_shark.size < shark.size:
                # 현재 상어를 넣어준다.
                shark.move_flag = True
                map_[tmp_x][tmp_y] = shark
                shark.x = tmp_x
                shark.y = tmp_y
                eat_shark_list.append(tmp_shark)
            else:
                # 작으면 사라진다.
                eat_shark_list.append(shark)
        else:
            shark.move_flag = True
            map_[tmp_x][tmp_y] = shark
            shark.x = tmp_x
            shark.y = tmp_y

    for shark in eat_shark_list:
        shark_list.remove(shark)

    # 이동여부 초기화.
    for shark in shark_list:
        shark.move_flag = False

    return map_, shark_list


def main():
    R, C, M = map(int, input().split())

    map_ = [[0]*C for _ in range(R)]

    shark_list = []

    for m in range(M):
        x, y, speed, arrow, size = map(int, input().split())

        shark = Shark(x-1, y-1, speed, arrow, size, False)
        map_[x-1][y-1] = shark
        shark_list.append(shark)

    shark_size_sum = 0

    # 사람이 한 칸씩 이동한다.
    for idx in range(C):

        # 해당 열에 상어가 있으면 잡는다.
        map_, shark_list, size = remove_shark(map_, shark_list, idx, R)

        shark_size_sum += size

        # 상어 이동.
        map_, shark_list = move_shark(map_, shark_list, R, C)

    print(shark_size_sum)


if __name__ == '__main__':
    main()
