# [아이디어]
# 연산자의 개수를 확인해 연산자들만 있는 리스트를 만들어 순열로 뽑아낸다.
# 숫자들을 하나씩 가져와 연산을 진행하여 res 리스트에 넣어둔다.
# 나누기 연산 시 a / b 에서 a가 음수일 경우 양수로 바꾸고 진행 후 음수로 변환한다.


nums = []
res = []


def perm(c, idx, save):
    global nums, res

    if idx == len(c):
        left = nums[0]
        idx = 0
        i = 1
        while i < len(nums):
            right = nums[i]
            if c[idx] == "+":
                left += right
            elif c[idx] == "-":
                left -= right
            elif c[idx] == "/":
                if left < 0:
                    left = -(left*(-1) // right)
                else:
                    left //= right
            elif c[idx] == "*":
                left *= right
            i += 1
            idx += 1

        res.append(left)

    for i in range(idx, len(c)):
        c[idx], c[i] = c[i], c[idx]
        perm(c, idx + 1, save)
        c[idx], c[i] = c[i], c[idx]


def main():
    global nums, res

    n = int(input())
    nums = list(map(int, input().split()))
    p, mi, mu, mo = map(int, input().split())
    c = []
    for i in range(p):
        c.append("+")
    for i in range(mi):
        c.append("-")
    for i in range(mu):
        c.append("*")
    for i in range(mo):
        c.append("/")

    perm(c, 0, nums)
    print(max(res))
    print(min(res))

if __name__ == '__main__':
    main()
