# 4

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/팀빌딩.txt")

input = file.readline 

n = int(input())
alist = list(map(int, input().split()))

result = 0
i, j = 0, n - 1
while i < j:
	result = max(result, (j-i-1) * min(alist[i], alist[j]))
	if alist[i] < alist[j]:
		i += 1
	elif alist[i] > alist[j]:
		j -= 1
	else:
		if alist[i+1] < alist[j-1]:
			i += 1
		else:
			j -= 1
print(result)

file.close()