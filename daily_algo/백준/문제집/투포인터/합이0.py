# 6

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/합이0.txt")

input = file.readline 

from collections import Counter

n = int(input())
alist = list(map(int, input().split()))
alist.sort()

count = Counter(alist)

result = 0
for i in range(n-2):
	l, r = i + 1, n - 1
	while l < r:
		value = alist[i] + alist[l] + alist[r]
		if value == 0:
			if alist[l] == alist[r]:
				result += r - l
			else:
				result += count[alist[r]]
			l += 1
		elif value < 0:
			l += 1
		else:
			r -= 1
print(result)
	

file.close()