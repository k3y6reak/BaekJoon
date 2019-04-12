# [아이디어]
# 카메라의 위치를 담을 클래스를 만들고, 그 개수를 세어준다.
# 카메라의 개수만큼 중복순열을 만들어준다.
# 이때 중복순열을 만들때 0, 1, 2, 3 요소로만 구성한다. (순서대로 상, 하, 좌, 우)
# 카메라의 돌면서 각 카메라의 종류별로 구분하여 상, 하, 좌, 우일때로 다시 구분하여 맵에 그려준다.
# 맵의 0의 개수를 세어 가장 작은 경우를 출력한다.

import itertools
import collections

low = 99999

class Camera:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

def show_up(map_, cam, X, Y):
    for i in range(cam.x, -1, -1):
        if map_[i][cam.y] == 0:
            map_[i][cam.y] = "#"
        elif map_[i][cam.y] == 6:
            break
        elif map_[i][cam.y] != 0 and map_[i][cam.y] != 6:
            continue

def show_down(map_, cam, X, Y):
    for i in range(cam.x, X):
        if map_[i][cam.y] == 0:
            map_[i][cam.y] = "#"
        elif map_[i][cam.y] == 6:
            break
        elif map_[i][cam.y] != 0 and map_[i][cam.y] != 6:
            continue

def show_left(map_, cam, X, Y):
    for j in range(cam.y, -1, -1):
        if map_[cam.x][j] == 0:
            map_[cam.x][j] = "#"
        elif map_[cam.x][j] == 6:
            break
        elif map_[cam.x][j] != 0 and map_[cam.x][j] != 6:
            continue


def show_right(map_, cam, X, Y):
    for j in range(cam.y, Y):
        if map_[cam.x][j] == 0:
            map_[cam.x][j] = "#"
        elif map_[cam.x][j] == 6:
            break
        elif map_[cam.x][j] != 0 and map_[cam.x][j] != 6:
            continue


def set_range_1(map_, cam, show, X, Y):
    if show == 0:
        show_up(map_, cam, X, Y)
    elif show == 1:
        show_down(map_, cam, X, Y)
    elif show == 2:
        show_left(map_, cam, X, Y)
    elif show == 3:
        show_right(map_, cam, X, Y)

def set_range_2(map_, cam, show, X, Y):
    if show == 0 or show == 1:
        show_up(map_, cam, X, Y)
        show_down(map_, cam, X, Y)
    elif show == 2 or show == 3:
        show_left(map_, cam, X, Y)
        show_right(map_, cam, X, Y)

def set_range_3(map_, cam, show, X, Y):
    if show == 0:
        show_up(map_, cam, X, Y)
        show_right(map_, cam, X, Y)
    elif show == 1:
        show_down(map_, cam, X, Y)
        show_left(map_, cam, X, Y)
    elif show == 2:
        show_up(map_, cam, X, Y)
        show_left(map_, cam, X, Y)
    elif show == 3:
        show_right(map_, cam, X, Y)
        show_down(map_, cam, X, Y)



def set_range_4(map_, cam, show, X, Y):
    if show == 0:
        show_up(map_, cam, X, Y)
        show_left(map_, cam, X, Y)
        show_right(map_, cam, X, Y)
    elif show == 1:
        show_down(map_, cam, X, Y)
        show_left(map_, cam, X, Y)
        show_right(map_, cam, X, Y)
    elif show == 2:
        show_up(map_, cam, X, Y)
        show_left(map_, cam, X, Y)
        show_down(map_, cam, X, Y)
    elif show == 3:
        show_up(map_, cam, X, Y)
        show_right(map_, cam, X, Y)
        show_down(map_, cam, X, Y)

def set_range_5(map_, cam, show, X, Y):
    show_up(map_, cam, X, Y)
    show_down(map_, cam, X, Y)
    show_left(map_, cam, X, Y)
    show_right(map_, cam, X, Y)

def print_map(map_, N, M):
    global low
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if map_[i][j] == 0:
                zero_cnt += 1

    low = min(low, zero_cnt)

def set_detection(map_, camera, show, camera_cnt, N, M):
    # 카메라 개수만큼 각 카메라의 감시 방향을 설정해주자.
    for i in range(camera_cnt):
        cam = camera[i]
        cam_num = cam.shape

        # 각 카메라 모양별로 세팅을 하자.
        if cam_num == 1:
            set_range_1(map_, cam, show[i], N, M)
        elif cam_num == 2:
            set_range_2(map_, cam, show[i], N, M)
        elif cam_num == 3:
            set_range_3(map_, cam, show[i], N, M)
        elif cam_num == 4:
            set_range_4(map_, cam, show[i], N, M)
        elif cam_num == 5:
            set_range_5(map_, cam, show[i], N, M)

    print_map(map_, N, M)

def set_map(map_, N, M):
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = map_[i][j]

    return tmp

def main():
    global low
    N, M = map(int, input().split())
    map_ = [[0]*M for _ in range(N)]

    # 전체 카메라의 개수를 뽑아낸다.
    camera_cnt = 0
    camera = collections.deque()
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            if line[j] != 0 and line[j] != 6:
                camera_cnt += 1
                camera.append(Camera(i, j, line[j]))
            map_[i][j] = line[j]

    # 카메라 개수만큼 상, 하, 좌, 우를 방향을 뽑아내는 중복순열.
    for i in itertools.product(range(4), repeat=camera_cnt):
        set_detection(set_map(map_, N, M), camera, i, camera_cnt, N, M)

    print(low)

if __name__ == '__main__':
    main()
