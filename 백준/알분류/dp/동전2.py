# 3

file = open("동전2.txt")

input = file.readline


def print_dp():
    print(* [i for i in range(k+1)])
    for i in range(k+1):
        if i > 9:
            print(dp[i], end="  ")
        else:
            print(dp[i], end=" ")
    print()


n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
for _ in range(n):
    value = int(input())
    for i in range(1, k//value+1):
        if i == 0 and dp[value*i] == i:
            break
        if dp[value*i] == 0:
            dp[value*i] = i
        else:
            dp[value*i] = min(dp[value*i], i)
        # print(value, i, value*i, dp[value*i])

for i in range(1, k+1):
    for j in range(1, i//2+1):
        if dp[i-j] != 0 and dp[j] != 0:
            if dp[i] == 0:
                dp[i] = dp[i-j] + dp[j]
            dp[i] = min(dp[i], dp[i-j] + dp[j])

print(dp[k] if dp[k] != 0 else -1)

# print_dp()

file.close()