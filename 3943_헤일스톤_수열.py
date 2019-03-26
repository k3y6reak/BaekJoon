# [아이디어]
# 주어진 규칙에 따라 값을 계산하면된다.
# 하지만, 입력한 수에 따라서 값이 엄청 크게 증가하는 경우가 발생하며 이 값이 다시 내려오는데 오래 걸린다.
# 넉넉히 300000까지 수를 돌리면서 해당 수를 규칙에 따라 진행하면서 그 값이 최초로 작아질 때를 구하고, 그 사이에 가장 큰 값을 구한다.
# 시작 수 부터 작아지는 수 사이의 최대 값을 구했으면 딕셔너리에 시작수: (작아지는 수, 최대 값) 형태로 저장한다.
# 특정 수 N에 대하여 찾는다면, 해당 값을 딕셔너리에서 찾아 최대 값을 찾고 다시 작아지는 수로 들어가 최대 값을 찾는 형식으로 재귀호출을 발생시켜 가장 큰 값을 찾았다.


import sys

d = {}


def find(n):
    global d

    big = n

    if d[n][0] != 1:
        big = max(d[n][1], find(d[n][0]))

    return big


def main():
    global d

    for n in range(1, 300001):
        save = n
        if n == 1:
            d[1] = (1, 1)
        else:
            big = n
            while n != 1:
                if n < save:
                    break
                if n & 1 == 1:
                    n = (n * 3) + 1
                    big = max(big, n)
                else:
                    n //= 2
                    big = max(big, n)

            d[save] = (n, big)

    for t in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        sys.stdout.write(str(find(n))+"\n")


if __name__ == '__main__':
    main()
