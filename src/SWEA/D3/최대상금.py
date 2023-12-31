#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645

file = open("./SWEA/D3/최대상금.txt", "r")

input = file.readline

import copy

def swap(number, i, j) :
	num = copy.deepcopy(number)
	temp = num[i]
	num[i] = num[j]
	num[j] = temp
	return ''.join(num)

def bfs(number, limit) : 

	q = set([number])
	p = set()

	length = len(number)

	for k in range(limit) :
		while q :
			num = list(q.pop())
			for i in range(length - 1) :
				for j in range(i + 1, length) :
					p.add(swap(num, i, j))
		q, p = p, q

	return max(q)
				

t = int(input())
for tc in range(1 , t + 1) : 
	number, limit = map(int, input().split())

	number = str(number)
	# print(number, limit)

	answer = bfs(number, limit)

	print("#%d %d" % (tc, int(answer)))
	print()
				

file.close()