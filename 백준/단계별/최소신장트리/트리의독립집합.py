# 10
# 2

# 0
# 1

# 10
# 2 or 1

# 10
# 1

# 140
# 1 3 5 7

import os

filename = "트리의독립집합.txt"
file = open(os.getcwd() + "\\" + filename)

input = file.readline

import sys

input = sys.stdin.readline


def trace(node, value):
    global visited

    if value <= 0:
        return

    temp = 0
    for next_node in adj[node]:
        if visited & 1 << next_node - 1 == 0:
            temp += dp[next_node][0]

    selected = False
    if value - weights[node] == temp:
        track.append(node)
        selected = True

    for next_node in adj[node]:
        if visited & 1 << next_node - 1 == 0:
            visited |= 1 << next_node - 1
            if selected:
                trace(next_node, value - weights[node])
            else:
                trace(next_node, dp[next_node][2])


def solve(node):
    global visited

    for next_node in adj[node]:
        if visited & 1 << next_node - 1 == 0:
            visited |= 1 << next_node - 1
            child = solve(next_node)
            dp[node][0] += child[-1]
            dp[node][1] += child[0]
    dp[node][1] += weights[node]
    if dp[node][0] < dp[node][1] or dp[node][0] == dp[node][1] == 0:
        dp[node][-1] = dp[node][1]
    else:
        dp[node][-1] = dp[node][0]
    return dp[node]

n = int(input())
weights = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
while True:
    line = input().strip()
    if line == "":
        break
    a, b = map(int, line.split())
    adj[a].append(b)
    adj[b].append(a)

# dp[n][0] : 정점 n이 S에 포함되지 않을 때 최대 S 크기
# dp[n][1] : 정점 n을 S에 포함시킬 때 최대 S 크기
# dp[n][2] : max(dp[n][0], dp[n][1])
# dp[n][2] : index(dp[n][2])
dp = [[0 for _ in range(3)] for _ in range(n + 1)]
initValue = 1

visited = initValue
solve(initValue)
print(dp[initValue][-1])

visited = initValue
track = []
trace(initValue, dp[initValue][-1])
track.sort()
print(*track)


file.close()
