# YES
# YES

import os
filename = "여행가자.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def find(num) :
    if parent[num] == num :
        return num
    return find(parent[num])

def union(num, set_num) :
    if find(num) == num :
        parent[num] = set_num
        return
    union(parent[num], set_num)

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
for i in range(1, n+1) :
    temp = list(map(int, input().split()))
    for j in range(n) :
        if temp[j] :
            adj[i].append(j+1)

paths = list(map(int, input().split()))

for ad in adj :
    print(ad)

parent = [i for i in range(n+1)]

for a in range(1, n+1) :
    fa = find(a)
    for b in adj[a] :
        fb = find(b)
        if fa == fb :
            continue
        elif fa < fb :
            union(b, fa)
        else :
            union(a, fb)

grand_parent = find(paths[0])
connected = True
for path in paths :
    if find(path) != grand_parent :
        connected = False
        break

print("YES" if connected else "NO")


file.close()