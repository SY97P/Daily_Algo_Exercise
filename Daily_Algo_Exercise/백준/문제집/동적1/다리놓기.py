# 1
# 5
# 67863915

file = open("./다리놓기.txt")

input = file.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0] = [i+1 for i in range(m)]
    for i in range(1, n):
        dp[i][i] = 1

    for i in range(1, n):
        for j in range(2, m):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    # for d in dp:
    #     print(d)

    print(dp[-1][-1])

file.close()