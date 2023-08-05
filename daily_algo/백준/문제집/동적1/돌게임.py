# SK

file = open("./돌게임.txt")

input = file.readline

for _ in range(6):
    n = int(input())

    dp = ["" for _ in range(n+1)]
    dp[-1] = "SK"

    for i in range(n, 0, -1):
        if i == 1:
            print(dp[i])
            break
        if dp[i] != "":
            dp[i-1] = dp[i-3] = "CY" if dp[i] == "SK" else "SK"

file.close()