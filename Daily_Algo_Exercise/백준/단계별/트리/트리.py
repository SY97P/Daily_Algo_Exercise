# Case 1: A forest of 3 trees.
# Case 2: There is one tree.
# Case 3: No trees.

import os
filename = "트리.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

# import sys
#
# input = sys.stdin.readline
#
# sys.setrecursionlimit(10**6)

def dfs(node, prev) :
    global visited, is_cycle

    for next_node in adj[node] :
        if visited & 1<<next_node-1 == 0 :
            visited |= 1<<next_node-1
            dfs(next_node, node)
        else :
            if next_node != prev :
                is_cycle = True

    # 현재 정점에서 연결된 곳 어디에도 갈 수 없었는데 심지어 갈 수 있는 곳이 두 개 이상이었다면
    # 고거슨 cycle
    # 나머지 상황
    # 1. 현재 정점에서 연결된 곳 다 갔다가 백트래킹으로 돌아감
    # 2. 연결된 곳이 없었음.
    # 3. 연결된 곳은 있었는데 갈 수 있는 곳이 한 군데였음. (방금 전 지나온 정점)


tc = 0
while True :
    tc += 1
    n, m = map(int, input().split())
    if n == m == 0 :
        break

    adj = [[] for _ in range(n+1)]
    for _ in range(m) :
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = 0
    count = 0
    for i in range(1, n+1) :
        if visited & 1<<i-1 == 0 :
            visited |= 1<<i-1
            is_cycle = False
            dfs(i, 0)
            if not is_cycle :
                count += 1

    print("Case %d:" % tc, end=" ")
    if count < 1 :
        print("No trees.")
    elif count < 2:
        print("There is one tree.")
    else :
        print("A forest of %d trees." % count)


file.close()