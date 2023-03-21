#1 43046721
#2 256
#3 7776
#4 10000000
#5 279936
#6 49
#7 43046721
#8 9
#9 65536
#10 262144

file = open("./SWEA/D3/거듭제곱.txt", "r")

input = file.readline

def recursion(n, dep) :
	if dep == 1: 
		return n

	return n * recursion(n, dep - 1)

for _ in range(10) : 
	tc = int(input())
	n, m = map(int, input().split())

	result = recursion(n, m)

	print("#%d %d" % (tc, result))

file.close()