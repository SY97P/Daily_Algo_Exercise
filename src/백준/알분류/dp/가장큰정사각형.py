# 4

file = open("./가장큰정사각형.txt")

input = file.readline

result = 0
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(map(int, input().strip()))
    if 1 in line:
        result = 1
    matrix.append(line)

dp = [[matrix[i][j] for j in range(m)] for i in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if matrix[i][j] != 0:
            if dp[i-1][j] != 0 and dp[i][j-1] != 0:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = 1
            result = max(result, dp[i][j])

print(result**2)

# for d in dp:
#     print(d)


file.close()