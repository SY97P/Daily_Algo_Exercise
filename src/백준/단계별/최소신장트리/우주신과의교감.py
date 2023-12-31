# 4.00

import os

filename = "우주신과의교감.txt"
file = open(os.getcwd() + "\\" + filename)

input = file.readline

import sys


# input = sys.stdin.readline


def find(num):
    if parent[num] == num:
        return num
    return find(parent[num])


def union(num, set_num):
    if parent[num] == num:
        parent[num] = set_num
        return
    union(parent[num], set_num)


def kruskal(lst):
    result = 0

    for cost, a, b in lst:
        fa, fb = find(a), find(b)

        if fa == fb:
            continue
        elif fa < fb:
            union(b, fa)
        else:
            union(a, fb)
        result += cost

    return result


def dist(a, b):
    return ((a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def getIdx(num):
    return num - 1


n, m = map(int, input().split())
gods = [[0] + list(map(int, input().split())) for _ in range(n)]
passed = [[0] + list(map(getIdx, map(int, input().split()))) for _ in range(m)]
parent = [i for i in range(n)]

edges = []
for i in range(n):
    for j in range(n):
        if i != j:
            edges.append([dist(gods[i], gods[j]), i, j])
edges.sort()

kruskal(passed)

print("%.2f" % kruskal(edges))

file.close()
