# 14000

import os
filename = "우수마을.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def solve(node):
    for next_node in adj[node]:
        if not visited[next_node]:
            visited[next_node] = True
            solve(next_node)
            dp[node][0] += max(dp[next_node])
            dp[node][1] += dp[next_node][0]
    dp[node][1] += w[node]


INIT_VALUE = 1
n = int(input())
w = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dp = [[0, 0] for _ in range(n+1)]

visited = [False for _ in range(n+1)]

visited[INIT_VALUE] = True
solve(INIT_VALUE)

# for d in dp:
#     print(d)

print(max(dp[INIT_VALUE]))


file.close()