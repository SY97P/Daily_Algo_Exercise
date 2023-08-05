# 2
# 3
# 4
# 2
# 2
# 4

import os
filename = "친구네트워크.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

import sys

input = sys.stdin.readline

def find(num) :
    if parent[num] == num :
        return num
    return find(parent[num])

def union(num, set_num) :
    family[set_num] += family[num]
    family[num] = 0
    if parent[num] == num :
        parent[num] = set_num
        return
    union(parent[num], set_num)

t = int(input())

for tc in range(t) :
    n = int(input())

    names = dict()
    count = 0

    parent = []
    family = []

    for _ in range(n) :
        me, you = input().split()
        a, b = 0, 0

        if me not in names.keys() :
            names[me] = count
            parent.append(count)
            family.append(1)
            count += 1
        a = names[me]

        if you not in names.keys() :
            names[you] = count
            parent.append(count)
            family.append(1)
            count += 1
        b = names[you]

        fa = find(a)
        fb = find(b)

        if a == b or fa == fb :
            print(family[find(b)])
        elif fa < fb :
            union(b, fa)
            print(family[find(a)])
        else :
            union(a, fb)
            print(family[find(b)])

        # print("parent : ", parent)
        # print("family : ", family)


file.close()