def solution(n, m, puddles):
    BOUND = 1_000_000_007

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[n][m] = 1

    for u, v in puddles:
        dp[u][v] = -1

    def dfs(x, y):
        if dp[x][y] == -1:
            return 0
        if dp[x][y] > 0:
            return dp[x][y]
        value = 0
        for dx, dy in ((0, 1), (1, 0)):
            if 0 < (di := x + dx) <= n and 0 < (dj := y + dy) <= m:
                if dp[di][dj] != -1:
                    value = (value + dfs(di, dj)) % BOUND
        dp[x][y] = value
        return dp[x][y]

    return dfs(1, 1)


def main():
    # answer = solution(4, 3, [[2, 2]])
    answer = solution(2, 2, [[1, 2]])
    print(answer)


if __name__ == '__main__':
    main()
