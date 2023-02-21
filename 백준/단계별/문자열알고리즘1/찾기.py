# 1
# 16

import os
filename = "찾기.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline


def get_pi(p, l):
    pi = [0 for _ in range(l)]
    j = 0
    for i in range(1, l):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(m, l):
    count = 0
    loc = []

    j = 0
    for i in range(m):
        # print(i, t[i], j, p[j])
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
            # print("rollback : ", i, t[i], j, p[j])
        if t[i] == p[j]:
            j += 1
            if j == l:
                j = pi[j-1]
                count += 1
                loc.append(i-l+2)
                # print(i, t[i], j, p[j], l, loc)

    print(count)
    print(*loc)


t = list(input().replace('\n', ''))
p = list(input().replace('\n', ''))

pi = get_pi(p, len(p))

# print(pi)

kmp(len(t), len(p))


file.close()
