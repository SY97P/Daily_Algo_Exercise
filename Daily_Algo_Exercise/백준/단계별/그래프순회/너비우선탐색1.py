# 1
# 2
# 4
# 3
# 0

file = open("C:/Users/onetu/PycharmProjects/Daily_Exercise_with_Programmers/백준/단계별/그래프순회/깊이우선탐색1.txt", "r")

input = file.readline

import sys
from collections import deque

input = sys.stdin.readline

def bfs(q) :
    count = 1

    dp = [0 for _ in range(n+1)]

    dp[q[0]] = count

    while q:
        node = q.popleft()

        for next_node in adj[node] :
            if dp[next_node] == 0 :
                count += 1
                dp[next_node] = count
                q.append(next_node)

    for d in dp[1:] :
        print(d)


n, m, r = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m) :
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n+1) :
    adj[i].sort()

bfs(deque([r]))

file.close()