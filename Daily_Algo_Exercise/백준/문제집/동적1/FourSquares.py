# 1
# 2
# 3
# 4

file = open("FourSquares.txt")

input = file.readline

for tc in range(4):
    n = int(input())

    dp = [0 for _ in range(n + 1)]
    prime = 0
    for i in range(1, n + 1):
        if i == (prime + 1) ** 2:
            dp[i] = 1
            prime += 1
            continue
        min_value = float('inf')
        for k in range(1, prime + 1):
            min_value = min(min_value, dp[i - k ** 2])
        dp[i] = 1 + min_value

    print(dp[n])

file.close()
