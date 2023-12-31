# -97 -2 98
# -6 -3 -2

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/세용액.txt")

input = file.readline

for _ in range(2):
	n = int(input())
	alist = list(map(int, input().split()))
	alist.sort()
	
	optimal = float('inf')
	result = [0, 0, 0]
	for i in range(n-2):
		l, r = i+1, n-1
		while l < r:
			value = alist[i] + alist[l] + alist[r]
			if optimal > abs(value):
				# print(optimal, abs(value), i, l, r, alist[i], alist[l], alist[r])
				optimal = abs(value)
				result = [i, l, r]
			if value <= 0:
				l += 1
			else: 
				r -= 1
	
	print(alist[result[0]], alist[result[1]], alist[result[2]])
	
file.close()