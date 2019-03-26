# [아이디어]
# 인원만큼의 리스트를 만들어 조합을 구한다. 이때 팀원 조합을 구하면 나머지 팀원을 뽑아내고 해당 팀을 뽑았다는 표시를 한다.
# 뽑아낸 팀원에서도 다시 조합을 구해 해당 인원의 가중치를 더한다.
# 스타트팀, 링크팀 모두 구해 차를 계산하고 절대값으로 변경하여 차이를 구한다.
# 해당 차이가 가장 작은 값을 출력한다.


from math import inf

vi = {}
low = inf

start_t_num = 0
link_t_num = 0


def comb2(map_, p, sel, idx, cnt, team):
    global start_t_num, link_t_num

    if cnt == len(sel):
        if team == "start":
            start_t_num += (map_[sel[0] - 1][sel[1]-1] + map_[sel[1] - 1][sel[0]-1])
        else:
            link_t_num += (map_[sel[0] - 1][sel[1] - 1] + map_[sel[1] - 1][sel[0] - 1])
        return

    if idx == len(p):
        return

    sel[cnt] = p[idx]
    comb2(map_, p, sel, idx + 1, cnt + 1, team)
    sel[cnt] = 0
    comb2(map_, p, sel, idx + 1, cnt, team)


def comb(map_, p, sel, idx, cnt):
    global vi, low, start_t_num, link_t_num

    if tuple(sel) in vi:
        return

    if cnt == len(sel):
        vi[tuple(sel)] = 1
        start_t = sel
        link_t = []
        for i in p:
            if i not in start_t:
                link_t.append(i)
        vi[tuple(link_t)] = 1

        comb2(map_, start_t, [False]*2, 0, 0, "start")
        comb2(map_, link_t, [False]*2, 0, 0, "link")
        num = abs(start_t_num - link_t_num)

        if num < low:
            low = num

        start_t_num, link_t_num = 0, 0
        return

    if idx == len(p):
        return

    sel[cnt] = p[idx]
    comb(map_, p, sel, idx + 1, cnt + 1)
    sel[cnt] = 0
    comb(map_, p, sel, idx + 1, cnt)


def main():
    global low

    map_ = [list(map(int, input().split())) for _ in range(int(input()))]
    n = len(map_)
    p = list(range(1, n+1))
    sel = [False]*(len(p)//2)

    comb(map_, p, sel, 0, 0)
    print(low)


if __name__ == '__main__':
    main()
