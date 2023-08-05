# 94
# 3234
# 775841

file = open("./Daily_Algo_Exercise/백준/문제집/그리디/크게만들기.txt")

input = file.readline 

from collections import deque

for _ in range(3):
	n, k = map(int, input().split())
	digit = list(input().strip())
	result = deque([])
	count = 0
	for d in digit:
		if count >= k:
			result.append(d)
		else:
			while result and count < k and result[-1] < d:
				result.pop()
				count += 1
			if len(result) < n - k:
				result.append(d)
	print(''.join(result))

file.close()