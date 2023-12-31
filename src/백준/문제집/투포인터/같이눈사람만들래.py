# 1

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/같이눈사람만들래.txt")

input = file.readline

n = int(input())
snows = list(map(int, input().split()))
snows.sort()

result = float('inf')
for i in range(n-1):
	for j in range(n-1, i, -1):
		ellsa = snows[i] + snows[j]
		l, r = 0, n-1
		while l == i or l == j:
			l += 1
		while r == i or r == j:
			r -= 1
		while l < r:
			while l == i or l == j:
				l += 1
			while r == i or r == j:
				r -= 1
			if l >= r:
				break
			anna = snows[l] + snows[r]
			result = min(result, abs(ellsa - anna))
			if ellsa <= anna:
				r -= 1
			else:
				l += 1
print(result)
		

file.close()