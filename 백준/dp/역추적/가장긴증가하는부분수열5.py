file = open("./백준/dp/역추적/가장긴증가하는부분수열4.txt", "r")

input = file.readline

def find(i) : 
	left, right = 0, len(lis) - 1
	while left < right : 
		mid = (left + right) // 2
		
		if lis[mid] < a[i] : 
			left = mid + 1
		else : 
			right = mid
			
	return right

n = int(input())
a = list(map(int, input().split()))

lis = [a[0]]

lis_index = [[0, 0] for _ in range(n)]
lis_index[0] = [0, a[0]]

for i in range(1, n) : 
	if lis[-1] < a[i] : 
		lis.append(a[i])
		lis_index[i] = [len(lis)-1, a[i]]
	else :
		j = find(i)
		lis[j] = a[i]
		lis_index[i] = [j, a[i]]

# print(lis)
# print(lis_index)

temp = []
index = len(lis) - 1

for i in range(n-1, -1, -1) :
	if index < 0 : 
		break

	if index == lis_index[i][0] : 
		index -= 1
		temp.append(lis_index[i][1])

print(len(temp))
print(*temp[::-1])

file.close()