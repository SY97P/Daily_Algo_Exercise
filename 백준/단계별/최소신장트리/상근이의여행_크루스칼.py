# 2
# 4

import os

filename = "상근이의여행.txt"
file = open(os.getcwd() + "\\" + filename)

input = file.readline

# * Kruskal 알고리즘
#     1. 모든 간선을 오름차순으로 정렬
#     2. 기존 MST 원소들과 사이클이 발생하지 않는 최소간선을 선택해 MST에 추가
#     3. 반복

import heapq, sys

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


t = int(input())

for tc in range(t):
    n, m = map(int, input().split())

    adj = []
    for _ in range(m):
        a, b = map(int, input().split())
        heapq.heappush(adj, (1, a, b))

    parent = [i for i in range(n+1)]

    count = 0

    while adj:
        cost, a, b = heapq.heappop(adj)

        fa, fb = find(a), find(b)

        # 문제에 a != b 조건 있음.
        if fa == fb:
            # 사이클 발생하므로 그냥 넘어감
            continue
        elif fa < fb:
            # 사이클 발생하지 않으므로 MST에 추가함 (MST의 대표 정점은 1이 됨)
            union(b, fa)
        else:
            union(a, fb)
        count += cost

    print(count)

file.close()
