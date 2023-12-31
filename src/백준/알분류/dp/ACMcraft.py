# 120
# 39
# 6
# 5
# 399990
# 2
# 0

file = open('./ACMcraft.txt')

input = file.readline


from collections import deque


def solve(q):
    result = -1
    while q:
        time, node = q.popleft()

        if time < dp[node]:
            continue
        if not adj[node]:
            result = max(result, dp[node], time)

        for require in adj[node]:
            if dp[require] < delay[require] + time:
                dp[require] = delay[require] + time
                q.append((dp[require], require))
    return result


t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    delay = [0] + list(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        adj[b].append(a)
    w = int(input())

    dp = [-1 for _ in range(n+1)]
    dp[w] = delay[w]

    print(solve(deque([(dp[w], w)])))



file.close()