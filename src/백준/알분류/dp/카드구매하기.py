# 10
# 50
# 55
# 50
# 20
# 18
# 520

file = open("카드구매하기.txt")

input = file.readline

for _ in range(7):
    n = int(input())
    p = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], p[j] + dp[i-j])
    print(dp)


file.close()