# 0
# 4

import os
filename = "사이클게임.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

import sys

input = sys.stdin.readline

def find(num) :
    if parent[num] == num :
        return num
    return find(parent[num])

def union(num, set_num) :
    if parent[num] == num :
        parent[num] = set_num
        return
    union(parent[num], set_num)

n, m = map(int, input().split())

parent = [i for i in range(n)]
result = 0

for count in range(1, m+1) :
    a, b = map(int, input().split())

    fa, fb = find(a), find(b)

    if fa == fb :
        if a == b :
            continue
        else :
            result = count
            break
    elif fa < fb :
        union(b, fa)
    else :
        union(a, fb)

print(result)

file.close()