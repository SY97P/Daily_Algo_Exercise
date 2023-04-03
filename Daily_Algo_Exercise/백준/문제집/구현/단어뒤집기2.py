# noojkeab enilno egduj
# <open>gat<close>

file = open("./Daily_Algo_Exercise/백준/문제집/구현/단어뒤집기2.txt")

input = file.readline

from collections import deque

for _ in range(2):
	line = input().strip()
	
	is_tag = False
	stack = deque([])
	
	for i, l in enumerate(line):
		if l == "<":
			is_tag = True
			while stack:
				print(stack.pop(), end="")
	
		if is_tag:
			print(l, end="")
		else:
			if l == " ":
				while stack:
					print(stack.pop(), end="")
				print("", end=" ")
			else:
				stack.append(l)
			
		if l == ">":
			is_tag = False
	while stack:
		print(stack.pop(), end="")
	print()
	

file.close()