# 1
# 0
# 0
# 3
# 2
# 4
# 1
# 4
# 3
# 2
# 0

file = open("C:/Users/onetu/PycharmProjects/Daily_Exercise_with_Programmers/백준/단계별/그래프순회/깊이우선탐색1.txt", "r")

input = file.readline

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

def dfs(node) :
    global count

    count += 1
    dp[node] = count

    # print(node, depth)

    for next_node in adj[node] :
        if dp[next_node] == 0 :
            dfs(next_node)

n, m, r = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m) :
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n+1) :
    adj[i].sort(reverse=True)

count = 0
dp = [0 for _ in range(n+1)]
dfs(r)

for d in dp[1:] :
    print(d)

file.close()
