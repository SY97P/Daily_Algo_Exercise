import os

file = open(os.getcwd()+"\러시아국기같은깃발.txt")

input = file.readline

from collections import Counter

dic = {0: 'W', 1: 'B', 2: 'R'}
t = int(input())
for tc in range(1, t+1):
    answer = 1e9

    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]

    counter = []

    for mat in matrix:
        counter.append(Counter(mat))

    temp = sum([v for k, v in counter[0].items() if k != 'W'])
    temp += sum([v for k, v in counter[-1].items() if k != 'R'])

    def get_cnt(clist):
        global answer
        idx = 0
        cnt = 0
        for i, count in enumerate(clist):
            for _ in range(count):
                idx += 1
                cnt += sum([v for k, v in counter[idx].items() if k != dic[i]])
        answer = min(answer, cnt)

    def dfs(idx, clist, bound):
        if sum(clist) > bound:
            return
        if idx == 3:
            if sum(clist) == bound and clist[1] != 0:
                get_cnt(clist)
            return
        for i in range(bound+1):
            nclist = clist.copy()
            nclist[idx] += i
            dfs(idx + 1, nclist, bound)

    dfs(0, [0, 0, 0], n-2)

    print(f'#{tc} {answer+temp}')


file.close()