# [아이디어]
# 주어진 숫자들 중에서 6개만 뽑아내면 된다.
# -> 조합을 사용하면 된다.

def comb(nums, sel, idx, cnt):
    if cnt == len(sel):
        for i in sel:
            print(str(i) + " ", end='')
        print()
        return

    if idx == len(nums):
        return

    sel[cnt] = nums[idx]
    comb(nums, sel, idx + 1, cnt + 1)
    sel[cnt] = 0
    comb(nums, sel, idx + 1, cnt)


def main():
    while True:
        line = list(map(int, input().split()))
        if len(line) != 1:
            n = line[0]
            nums = line[1:]
            comb(nums, [False]*6, 0, 0)
            print()
        else:
            break


if __name__ == '__main__':
    main()
