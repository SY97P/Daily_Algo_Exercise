# 6

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/합이0.txt")

input = file.readline 

n = int(input())
alist = list(map(int, input().split()))
alist.sort()

result = 0
for i in range(n-2):
	l, r = i+1, n-1
	while l < r:
		value = alist[i] + alist[l] + alist[r]
		if value == 0:
			result += 1
		elif value > 0:
			

file.close()