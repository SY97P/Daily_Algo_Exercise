# 3

import os
filename = "최소스패닝트리.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

# * Prim 알고리즘
#     1. MST에 임의의 정점 하나를 추가
#     2. MST의 정점과 아닌 정점 간 간선 중에 최소값을 선택
#     3. 반복

import heapq, sys

input = sys.stdin.readline

def prim() :
    q = [(0, 1)]
    heapq.heapify(q)

    MST = [False for _ in range(v+1)]
    result = 0

    while q :
        cost, node = heapq.heappop(q)

        if not MST[node] :
            MST[node] = True
            result += cost

            for next_cost, next_node in adj[node] :
                if not MST[next_node] :
                    heapq.heappush(q, (next_cost, next_node))

    return result


v, e = map(int, input().split())

adj = [[] for _ in range(v+1)]
for _ in range(e) :
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

print(prim())

file.close()