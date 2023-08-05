file = open("./Daily_Algo_Exercise/SWEA/D3/조합.txt")

input = file.readline

mod = 1234567891
def pow(num, p):
	if p == 0:
		return 1
	half = pow(num, p//2)
	if p % 2 == 0:
		return (half%mod) * (half%mod) % mod
	else:
		return ((half*num)%mod) * (half%mod) % mod

t = int(input())
for tc in range(1, t+1):
	n, r = map(int, input().split())
	dp = [1] * (n+1)
	for i in range(2, n+1):
		dp[i] = (dp[i-1] * i) % mod

	top = dp[n]%mod
	bottom = ((dp[r]%mod) * (dp[n-r]%mod))%mod

	perma_top = pow(bottom, mod-2)

	print(f'#{tc} {int(top * perma_top)%mod}')

file.close()