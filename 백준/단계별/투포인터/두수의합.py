# 3

file = open("./백준/투포인터/두수의합.txt", "r")

input = file.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

i, j = 0, n-1

count = 0 

a.sort()

while i < j : 
	# print(i, a[i], j, a[j], " : ", a[i] + a[j])
	if a[i] + a[j] == x : 
		count += 1
		i += 1
		j -= 1
	elif a[i] + a[j] > x : 
		j -= 1
	else : 
		i += 1

print(count)

file.close()