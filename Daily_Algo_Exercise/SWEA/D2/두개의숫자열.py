#1 30
#2 63
#3 140
#4 181
#5 63
#6 58
#7 22
#8 120
#9 96
#10 70

file = open("./SWEA/D2/두개의숫자열.txt", "r")

input = file.readline

t = int(input())

def cal(alist, blist) :
	result = 0
	for i in range(len(alist)) : 
		result += alist[i] * blist[i]
	return result

for tc in range(1, t + 1) : 
	n, m = map(int, input().split())
	alist = list(map(int, input().split()))
	blist = list(map(int, input().split()))

	# print(n, m)
	# print(alist)
	# print(blist)
	# print()

	result = 0

	if n == m : 
		result = cal(n, alist, blist)
	else : 
		if n > m : 
			temp = n
			n = m
			m = temp
			temp = alist
			alist = blist
			blist = temp
	for i in range(m - n + 1) : 
			result = max(result, cal(alist, blist[i:]))

	print("#%d %d" % (tc, result))

file.close()