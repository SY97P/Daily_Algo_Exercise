# 2

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/부분합.txt")

input = file.readline

n, s = map(int, input().split())
alist = list(map(int, input().split()))
asum = [0]
for a in alist:
	asum.append(asum[-1] + a)

result = float('inf')
i, j = 0, 1
while j <= n:
	if asum[j] - asum[i] < s:
		j += 1
	elif asum[j] - asum[i] >= s:
		result = min(result, j - i)
		i += 1
print(result if result != float('inf') else 0)


file.close()