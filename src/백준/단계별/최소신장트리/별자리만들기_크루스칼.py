# 3.41

import os
filename = "별자리만들기.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

# import sys
#
# input = sys.stdin.readline

# * Kruskal 알고리즘
#     1. 모든 간선을 가중치 기준 오름차순 정렬
#     2. MST에 사이클이 생기지 않는 선에서 최소 간선을 선택해 MST에 추가
#     3. 모든 정점이 MST에 포함되도록 반복


def find(num) :
    if parent[num] == num :
        return num
    return find(parent[num])


def union(num, set_num) :
    if parent[num] == num :
        parent[num] = set_num
        return
    union(parent[num], set_num)


def kruskal() :
    global parent

    parent = [i for i in range(n)]
    result = 0

    for c, a, b in edges :
        fa, fb = find(a), find(b)

        if fa == fb :
            continue
        elif fa < fb :
            union(b, fa)
        else :
            union(a, fb)
        result += c
    return result


def dist(a, b) :
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


n = int(input())

stars = [tuple(map(float, input().split())) for _ in range(n)]

edges = []
for i in range(n) :
    for j in range(n) :
        if i != j :
            edges.append((dist(stars[i], stars[j]), i, j))
edges.sort()

print("%.2f" % kruskal())


file.close()