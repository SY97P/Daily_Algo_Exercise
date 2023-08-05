#1 71
#2 76
#3 79
#4 80
#5 52
#6 66
#7 35
#8 97
#9 92
#10 72

file = open("./SWEA/D2/최빈수구하기.txt", "r")

input = file.readline

from collections import defaultdict

t = int(input())
for _ in range(t) : 
	no = int(input())
	numbers = list(map(int, input().split()))

	dic = defaultdict(int)

	for num in numbers : 
		dic[num] += 1

	key = value = 0 
	for k in dic.keys() :
		if dic[k] > value : 
			value = dic[k]
			key = k

	print("#%d %d" % (no, key))

file.close()