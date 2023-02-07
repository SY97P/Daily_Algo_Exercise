# 2
# 4

import os
filename = "상근이의여행.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

# * Prim 알고리즘
#     1. MST에 아무 정점 하나를 포함시킴
#     2. MST 구성하는 원소와 아닌 원소 간 최소 간선을 이루는 정점을 MST에 추가
#     3. 반복

import heapq, sys

# input = sys.stdin.readline

def prim(init) :
    visited = [False for _ in range(n+1)]
    visited[init] = True

    q = [init]
    heapq.heapify(q)

    MST = [init]
    count = 0

    while q :
        node = heapq.heappop(q)

        for next_node in adj[node] :
            if next_node not in MST :
                MST.append(next_node)
                heapq.heappush(q, next_node)
                count += 1

    return count



t = int(input())

for tc in range(t) :
    n, m = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    for _ in range(m) :
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    print(prim(1))


file.close()