from itertools import product


class Board:
    def __init__(self, score, link_turn, link_go, unit_idx):
        self.score = score
        self.link_turn = link_turn
        self.link_go = link_go
        self.unit_idx = unit_idx


class Unit:
    def __init__(self, idx, current):
        self.idx = idx
        self.current = current
# 맵 세팅


B21 = Board(0, None, None, 0)
B20 = Board(40, None, B21, 0)
B29 = Board(35, None, B20, 0)
B28 = Board(30, None, B29, 0)
B27 = Board(25, None, B28, 0)
B24 = Board(19, None, B27, 0)
B23 = Board(16, None, B24, 0)
B22 = Board(13, None, B23, 0)
B26 = Board(24, None, B27, 0)
B25 = Board(22, None, B26, 0)
B32 = Board(26, None, B27, 0)
B31 = Board(27, None, B32, 0)
B30 = Board(28, None, B31, 0)
B19 = Board(38, None, B20, 0)
B18 = Board(36, None, B19, 0)
B17 = Board(34, None, B18, 0)
B16 = Board(32, None, B17, 0)
B15 = Board(30, B30, B16, 0)
B14 = Board(28, None, B15, 0)
B13 = Board(26, None, B14, 0)
B12 = Board(24, None, B13, 0)
B11 = Board(22, None, B12, 0)
B10 = Board(20, B25, B11, 0)
B9 = Board(18, None, B10, 0)
B8 = Board(16, None, B9, 0)
B7 = Board(14, None, B8, 0)
B6 = Board(12, None, B7, 0)
B5 = Board(10, B22, B6, 0)
B4 = Board(8, None, B5, 0)
B3 = Board(6, None, B4, 0)
B2 = Board(4, None, B3, 0)
B1 = Board(2, None, B2, 0)
B0 = Board(0, None, B1, 0)


def init_units(units):
    """
    :param units: 중복순열
    :return: Unit 객체가 저장된 배열
    """
    unit_1 = Unit(1, B0)
    unit_2 = Unit(2, B0)
    unit_3 = Unit(3, B0)
    unit_4 = Unit(4, B0)

    for i in range(10):
        if units[i] == 1:
            units[i] = unit_1
        elif units[i] == 2:
            units[i] = unit_2
        elif units[i] == 3:
            units[i] = unit_3
        elif units[i] == 4:
            units[i] = unit_4

    return units


def board_clear(used_board):
    for b in used_board:
        b.unit_idx = 0


def move_units(units, moves):
    total_score = 0

    # 사용된 말
    finished_unit = []

    # 사용된 보드
    used_board = []

    for i in range(10):
        # 현재 말
        unit = units[i]

        # 이동하고자하는 말이 사용된 말이면 진행 불가.
        if unit.idx in finished_unit:
            # 보드가 전역이므로 전부 초기화.
            board_clear(used_board)
            return 0, (units, i)
        else:
            # 말의 현재 위치를 저장한다.
            unit_current = unit.current

            # 주어진 주사위 수 만큼 이동한다.
            for move in range(moves[i]):
                # 이동하고자 하는 말의 처음 위치를 0으로 초기화.
                # 만약, 이동 중에 마지막에 도착한 경우(B21).
                if unit.current == B21:
                    unit.current.unit_idx = 0

                    # 도착한 말 저장.
                    finished_unit.append(unit.idx)

                    # 더 이상 이동하지 않아도 된다.
                    break

                # 첫 출발이면서, 위치가 꺽는 곳이면(B5, B10, B15) 방향을 바꾼다.
                if move == 0 and unit.current in [B5, B10, B15]:
                    # 다음 위치로 이동한다.
                    unit.current = unit.current.link_turn

                    # 보드 초기화를 위해 해당 보드 저장.
                    used_board.append(unit.current)

                # 첫 출발이 꺽는위치가 아닌경우, 그대로 이동하는 경우.
                else:
                    # 다음 위치로 이동한다.
                    unit.current = unit.current.link_go

                    # 보드 초기화를 위해 해당 보드 저장.
                    used_board.append(unit.current)

            # 이동 후, 해당 보드에 다른 말이 존재한다면 이동불가.
            if unit.current.unit_idx != 0:
                # 보드가 전역이므로 전부 초기화.
                board_clear(used_board)
                return 0, (units, i)

            # 다른 말이 없다면, 해당 위치 확정.
            else:
                # 해당 위치가 도착지점이면
                if unit.current == B21:
                    unit.current.unit_idx = 0
                    used_board.append(unit.current)
                    finished_unit.append(unit.idx)
                else:
                    # 해당 위치에 말 저장.
                    unit.current.unit_idx = unit.idx

                # 처음 시작 위치를 0으로 변경.
                unit_current.unit_idx = 0

                # 해당 위치의 점수 저장.
                total_score += unit.current.score

    # 보드가 전역이므로 전부 초기화.
    board_clear(used_board)
    return total_score, None


def main():
    moves = [int(_) for _ in input().split()]
    max_score = 0
    failed_units, failed_idx = None, None
    cnt = 0

    for units in product(range(1, 5), repeat=10):
        # 실패한 말이 계속 사용될 필요 없음.

        if failed_units and failed_idx:
            for idx in range(failed_idx):
                if units[idx] == failed_units[idx]:
                    cnt += 1
            if cnt == failed_idx - 1:
                continue

        # unit 초기화
        units = init_units(list(units))

        # unit 이동
        total_score, failed = move_units(units, moves)

        if failed:
            failed_units, failed_idx = failed[0], failed[1]

        max_score = max(max_score, total_score)

    print(max_score)


if __name__ == '__main__':
    main()
