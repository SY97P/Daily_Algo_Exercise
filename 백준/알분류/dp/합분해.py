# 21
# 84

file = open("./합분해.txt")

input = file.readline

for _ in range(2):
    n, k = map(int, input().split())

    dp = [[1 for _ in range(n+1)] for _ in range(k+1)]

    for i in range(2, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            # print(i, j, dp[i-1][j], dp[i][j-1], dp[i][j])

    print(dp[-1][-1]%1000000000)

    # for d in dp:
    #     print(d)

file.close()