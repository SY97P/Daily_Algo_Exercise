import sys
sys.setrecursionlimit(10**6)


def solution(n, m, puddles):
    BOUND = 1e9 + 7

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[n][m] = 1

    def dfs(x, y):
        if dp[x][y] < 0:
            return 0
        elif dp[x][y] > 0:
            return dp[x][y]
        value = 0
        for dx, dy in ((0, 1), (1, 0)):
            if 0 < (di := x + dx) <= n and 0 < (dj := y + dy) <= m and dp[di][dj] > -1:
                value += dfs(di, dj)
        dp[x][y] = value
        return dp[x][y]

    answer = dfs(1, 1)

    for d in dp:
        print(d)

    return answer


def main():
    answer = solution(4, 3, [[2, 2]])
    print(answer)


if __name__ == '__main__':
    main()
