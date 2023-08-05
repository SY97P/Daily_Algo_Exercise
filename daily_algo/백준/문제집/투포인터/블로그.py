# 7
# 1

# 9
# 2

# SAD

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/블로그.txt")

input = file.readline

for _ in range(1):
	n, x = map(int, input().split())
	visitor = list(map(int, input().split()))
	asum = [0]
	for v in visitor:
		asum.append(asum[-1] + v)
	
	max_v = 0
	count = 0
	for i in range(x, n+1):
		# print(asum[i] - asum[i-x])
		if max_v < asum[i] - asum[i-x]:
			max_v = asum[i] - asum[i-x]
			count = 1
		elif max_v == asum[i] - asum[i-x]:
			count += 1

	if max_v != 0:
		print(max_v)
		print(count)
	else:
		print("SAD")
	

file.close()