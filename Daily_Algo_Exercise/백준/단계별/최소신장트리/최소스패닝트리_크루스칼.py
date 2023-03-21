# 3

import os
filename = "최소스패닝트리.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

# * Kruskal 알고리즘
#     1. 모든 간선 오름차순 정렬
#     2. MST에 사이클이 생기지 않는 최소간선 선택해 MST에 추가
#     3. 반복

import sys
from collections import deque

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


def kruskal(adj) :
    global parent

    parent = [i for i in range(v+1)]

    result = 0

    while adj :
        cost, a, b = adj.popleft()

        fa, fb = find(a), find(b)

        if fa == fb :
            continue
        elif fa < fb :
            union(b, fa)
        else :
            union(a, fb)
        result += cost
    return result


v, e = map(int, input().split())

adj = []
for _ in range(e) :
    a, b, c = map(int, input().split())
    adj.append((c, a, b))
adj.sort()
adj = deque(adj)

print(kruskal(adj))

file.close()