from heapq import heappush, heappop


def solution(n, edge):
    dp = [1e9]*(n+1)
    dp[0] = dp[1] = 0

    adj = [[] for _ in range(n+1)]
    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)

    q = [(0, 1)]

    while q:
        dist, node = heappop(q)
        if dp[node] < dist:
            continue
        for next_node in adj[node]:
            if dp[next_node] > dist + 1:
                dp[next_node] = dist + 1
                heappush(q, (dp[next_node], next_node))

    return dp.count(max(dp))


def main():
    answer = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
    print(answer)


if __name__ == '__main__':
    main()