# [아이디어]
# 주사위의 각 위치마다 값을 저장할 리스트를 만든다.
# 특정 방향에 따른 위치가 어떻게 변하는지 잘 생각하면 된다.


# 위, 앞, 왼, 오, 뒤 , 아래
dice = [0, 0, 0, 0, 0, 0]

up = 0
front = 1
left = 2
right = 3
back = 4
down = 5


def map_chk(map_, x, y):
    global dice

    if map_[x][y] == 0:
        map_[x][y] = dice[down]
    else:
        dice[down] = map_[x][y]
        map_[x][y] = 0


def range_chk(x, y, n, m, c):
    if c == 1:
        if y + 1 < m:
            return True
        else:
            return False

    elif c == 2:
        if y - 1 >= 0:
            return True
        else:
            return False

    elif c == 3:
        if x - 1 >= 0:
            return True
        else:
            return False

    elif c == 4:
        if x + 1 < n:
            return True
        else:
            return False


def main():
    global dice, up, front, left, right, back, down

    n, m, x, y, k = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    cmd = list(map(int, input().split()))
    tmp_dice = [0, 0, 0, 0, 0, 0]

    for c in cmd:
        #여기에 범위 체크 해보자!
        if range_chk(x, y, n, m, c):
            if c == 1:
                # 동쪽으로 이동하면 왼->위 / 위->오 / 오->아래 / 앞->앞 / 뒤->뒤 / 아래->왼
                tmp_dice[up] = dice[left]
                tmp_dice[right] = dice[up]
                tmp_dice[down] = dice[right]
                tmp_dice[left] = dice[down]
                tmp_dice[back] = dice[back]
                tmp_dice[front] = dice[front]

                # tmp_dice에서 dice로 이동, tmp_dice 초기화
                for i in range(len(dice)):
                    dice[i] = tmp_dice[i]
                    tmp_dice[i] = 0

                y += 1
                map_chk(map_, x, y)

            elif c == 2:
                # 서쪽으로 이동하면 위->왼 / 오->위 / 아래->오 / 앞->앞 / 뒤->뒤 / 왼->아래
                tmp_dice[left] = dice[up]
                tmp_dice[down] = dice[left]
                tmp_dice[right] = dice[down]
                tmp_dice[up] = dice[right]
                tmp_dice[front] = dice[front]
                tmp_dice[back] = dice[back]

                # tmp_dice에서 dice로 이동, tmp_dice 초기화
                for i in range(len(dice)):
                    dice[i] = tmp_dice[i]
                    tmp_dice[i] = 0

                y -= 1
                map_chk(map_, x, y)

            elif c == 3:
                # 북쪽으로 이동하면 앞->위 / 왼->왼 / 오->오 / 뒤->아래 / 아래->앞 / 위-> 뒤
                tmp_dice[up] = dice[front]
                tmp_dice[back] = dice[up]
                tmp_dice[down] = dice[back]
                tmp_dice[front] = dice[down]
                tmp_dice[left] = dice[left]
                tmp_dice[right] = dice[right]

                # tmp_dice에서 dice로 이동, tmp_dice 초기화
                for i in range(len(dice)):
                    dice[i] = tmp_dice[i]
                    tmp_dice[i] = 0

                x -= 1
                map_chk(map_, x, y)

            elif c == 4: # 남쪽이동
                # 남쪽으로 이동하면 위->앞 / 왼->왼 / 오->오 / 아래->뒤 / 앞->아래 / 뒤->위
                # dice에서 tmp_dice로 넣는다.
                tmp_dice[front] = dice[up]
                tmp_dice[down] = dice[front]
                tmp_dice[back] = dice[down]
                tmp_dice[up] = dice[back]
                tmp_dice[right] = dice[right]
                tmp_dice[left] = dice[left]

                # tmp_dice에서 dice로 이동, tmp_dice 초기화
                for i in range(len(dice)):
                    dice[i] = tmp_dice[i]
                    tmp_dice[i] = 0

                x += 1
                map_chk(map_, x, y)
            print(dice[up])


if __name__ == '__main__':
    main()
