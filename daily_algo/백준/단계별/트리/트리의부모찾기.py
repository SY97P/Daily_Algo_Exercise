# 4
# 6
# 1
# 3
# 1
# 4
# 1
# 1
# 2
# 3
# 3
# 4
# 4
# 5
# 5
# 6
# 6

import os

filename = "트리의부모찾기.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

def solve(node) :
    global visited

    for next_node in adj[node] :
        if visited & 1<<next_node-1 == 0 :
            visited |= 1<<next_node-1
            dp[next_node] = node
            solve(next_node)


n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = 1
dp = [0 for _ in range(n+1)]
solve(1)

for d in dp[2:] :
    print(d)

file.close()