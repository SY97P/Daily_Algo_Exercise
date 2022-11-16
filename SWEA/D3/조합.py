#1 45

file = open("./SWEA/D3/조합.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	n, r = map(int, input().split())

	sumof = 1

	temp = n

	while temp > n - r : 
		sumof *= temp
		temp -= 1
	
	while r > 0 : 
		sumof //= r
		r -= 1

	print("#%d %d" %(tc, sumof % 1234567891))

file.close()