# 5
# 4

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/회전초밥.txt")

input = file.readline 

n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]

result = 0
count_list = [0 for _ in range(d + 1)]
for aa in a[:k]:
	if count_list[aa] == 0:
		result += 1
	count_list[aa] += 1
if count_list[c] == 0:
	count_list[c] = 1
	result += 1
count = result
	
for i in range(1, n):
	j = (i + k - 1) % n
	count_list[a[i-1]] -= 1
	if count_list[a[i-1]] == 0:
		# print("A")
		count -= 1
	if count_list[a[j]] == 0:
		# print("B")
		count += 1
	count_list[a[j]] += 1
	if count_list[c] == 0:
		count_list[c] = 1
		# print("C")
		count += 1
	# print(count_list)
	# print("count_list: ", end="")
	# for l, co in enumerate(count_list):
	# 	if co != 0:
	# 		print(l, end=" ")
	# print()
	# print(a[i:j+1])
	# print(i, j, count, result)
	result = max(result, count)

print(result)

file.close()