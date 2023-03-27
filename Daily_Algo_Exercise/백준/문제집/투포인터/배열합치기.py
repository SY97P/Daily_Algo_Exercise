# 2 3 5 9
# 1 4 7
# 1 2 3 4 5 7 9

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/배열합치기.txt")

input = file.readline

for _ in range(3):
	n, m = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	
	i = j = 0
	result = []
	
	while True:
		if i >= n:
			result += b[j:]
			break
		if j >= m:
			result += a[i:]
			break
		if a[i] < b[j]:
			result.append(a[i])
			i += 1
		else:
			result.append(b[j])
			j += 1
	
	print(* result)
	

file.close()