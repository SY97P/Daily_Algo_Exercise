def solution(n, s, a, b, fares):
    dp = [[1e9] * (n + 1) for _ in range(n + 1)]

    for u, v, c in fares:
        dp[u][v] = c
        dp[v][u] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dp[i][j] = 0
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return min([dp[s][i] + dp[i][a] + dp[i][b] for i in range(1, n + 1)])


def main():
    answer = solution(6, 4, 6, 2,
                      [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                       [1, 6, 25]])
    print(answer)


if __name__ == '__main__':
    main()
