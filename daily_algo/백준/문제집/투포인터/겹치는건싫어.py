# 7
# 6

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/겹치는건싫어.txt")

input = file.readline 

for _ in range(2):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	count = [0 for _ in range(max(a) + 1)]
	result = 0
	
	i = j = 0
	while j < n:
		if count[a[j]] < k:
			count[a[j]] += 1
			j += 1
		else:
			count[a[i]] -= 1
			i += 1
		result = max(result, j - i)
	print(result)

file.close()