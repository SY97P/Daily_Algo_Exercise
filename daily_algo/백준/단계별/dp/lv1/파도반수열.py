# 3
# 16

file = open("./백준/dp/파도반수열.txt", "r")

input = file.readline

t = int(input())

p = [1, 1, 1, 2, 2]

for i in range(5, 101) :
	p.append(p[i-3] + p[i-2])

for tc in range(t) : 
	n = int(input())
	print(p[n-1])

file.close()