# 45
# 55
# 20
# 90

file = open("퇴사.txt")

input = file.readline


for _ in range(1):
    n = int(input())
    t, p = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)
    dp = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        if i+t[i] <= n:
            dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])
        else:
            dp[i] = dp[i+1]

    print(dp[0])



file.close()