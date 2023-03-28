# -99 98

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/두용액.txt")

input = file.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

value = float('inf')
result_i, result_j = 0, n - 1
i, j = 0, n-1
while i < j:
	temp = a[i] + a[j]
	if temp == 0:
		result_i, result_j = i, j
		break
	if temp < 0:
		if abs(temp) < value:
			value = abs(temp)
			result_i, result_j = i, j
		i += 1
	else:
		if abs(temp) < value:
			value = abs(temp)
			result_i, result_j = i, j
		j -= 1
			
print(a[result_i], a[result_j])
	

file.close()