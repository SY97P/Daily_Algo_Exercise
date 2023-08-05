# 1
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 1
# 0
# 0
# 0
# 1
# 0

file = open("./백준/dp/lv3/집합.txt", "r")

input = file.readline

# import sys

# input = sys.stdin.readline

n = int(input())

s = 1

for _ in range(n) : 
	oper = input().split()

	# print(oper)

	if oper[0] == "all" :
		s = (1 << 20) - 1
	elif oper[0] == "empty" : 
		s = 0
	elif oper[0] == "add" : 
		s |= (1 << int(oper[1]) - 1)
	elif oper[0] == "remove" :
		s &= ~(1 << int(oper[1]) - 1)
	elif oper[0] == "check" : 
		# print(int(oper[1]), int(oper[1]) - 1, " -> ", bin(1 << int(oper[1]) - 1))
		if s & (1 << int(oper[1]) - 1) == 0 :
			print(0)
		else : 
			print(1)
	elif oper[0] == "toggle" :
		s ^= (1 << int(oper[1]) - 1)

	# print(bin(s))

file.close()