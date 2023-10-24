def solution(n, results):
    dp = [['?'] * (n + 1) for _ in range(n + 1)]

    for a, b in results:
        dp[a][b] = 'win'
        dp[b][a] = 'lose'

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dp[i][i] = 'self'
                if dp[i][k] == 'win' and dp[k][j] == 'win':
                    dp[i][j] = 'win'
                elif dp[i][k] == 'lose' and dp[k][j] == 'lose':
                    dp[i][j] = 'lose'

    return sum([1 if d.count('?') <= 1 else 0 for d in dp])


def main():
    answer = solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
    print(answer)


if __name__ == '__main__':
    main()
