# 3

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/가장긴짝수연속한부분수열_large.txt")

input = file.readline 

n, k = map(int, input().split())
a = list(map(int, input().split()))

length = count = 0
i = j = 0
while True:
	print(i, j, a[i], a[j], length, count)
	while (j < n-1):
		if a[j+1] % 2 != 0:
			if count < k:
				print("shit: ", i, j, a[i], a[j], length, count)
				count += 1
			else:
				break
		j += 1
	if i >= n or j >= n:
		break
	length = max(length, j - i + 1 - count)
	if a[i] % 2 != 0:
		count -= 1
	i += 1
	
print(i, j, length)

file.close()