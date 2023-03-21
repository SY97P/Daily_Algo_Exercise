# 3

# 3

import os
filename = "사회망서비스(SNS).txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def solve(node):
    for next_node in adj[node]:
        if not visited[next_node]:
            visited[next_node] = True
            solve(next_node)
            dp[node][0] += dp[next_node][1]
            dp[node][1] += min(dp[next_node])


initValue = 1
n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dp = [[0, 1] for _ in range(n+1)]

visited = [False for _ in range(n+1)]

visited[initValue] = True
solve(initValue)

print(min(dp[initValue]))


file.close()