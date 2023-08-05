# 3.41

import os
filename = "별자리만들기.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

# * Prim 알고리즘
#     1. MST에 임의의 한 점 추가
#     2. MST에 포함된 정점들과 아닌 정점간 최소 간선인 정점을 MST에 추가 (힙큐 사용)
#     3. 반복

import heapq, sys

input = sys.stdin.readline

def dist(a, b) :
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def prim() :
    q = [(0, 0)]
    heapq.heapify(q)

    visited = [False for _ in range(n)]

    result = 0

    while q :
        cost, node = heapq.heappop(q)

        if not visited[node] :
            visited[node] = True
            result += cost

        for next_cost, next_node in adj[node] :
            if not visited[next_node] :
                heapq.heappush(q, (next_cost, next_node))

    return result


n = int(input())

stars = []
for _ in range(n) :
    a, b = map(float, input().split())
    stars.append((a, b))

adj = [[] for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if i != j :
            adj[i].append((dist(stars[i], stars[j]), j))

# for ad in adj :
#     print(ad)

print("%.2f" % prim())


file.close()