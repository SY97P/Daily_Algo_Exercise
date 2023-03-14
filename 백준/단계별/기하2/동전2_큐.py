file = open("./동전2.txt")

input = file.readline


from collections import deque

n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
q = deque([])
coins = set()
for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.add(coin)
        dp[coin] = 1
        q.append((coin, dp[coin]))

coins = sorted(coins)

while q:
    val, count = q.popleft()
    if val > k:
        continue
    for coin in coins:
        c = val + coin
        if c > k:
            break
        if dp[c] == 0:
            dp[c] = count + 1
            q.append((c, dp[c]))
print(dp[-1] if dp[-1] != 0 else -1)

print(dp)


file.close()