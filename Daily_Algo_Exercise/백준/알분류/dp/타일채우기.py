# 3
# 11
# 41
# 159
# ?

file = open('./타일채우기.txt')

input = file.readline


def solve(n):
    if n % 2 != 0:
        return 0
    if dp[n] != 0:
        return dp[n]
    dp[n] = solve(n-2) * solve(2)
    # print(dp[n])
    for i in range(n-3):
        dp[n] += 2 * solve(i)
    return dp[n]


for _ in range(1):
    n = int(input())
    dp = [0 for i in range(n+1 if n > 1 else 3)]
    dp[0], dp[2] = 1, 3

    print(solve(n))

    # print(dp)


file.close()