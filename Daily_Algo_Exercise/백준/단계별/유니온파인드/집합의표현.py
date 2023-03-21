# NO(no)
# NO(no)
# YES(yes)

# YES
# YES
# NO
# YES
# YES
# YES
# NO
# NO
# YES

import os

file = open("./백준/단계별/유니온파인드/집합의표현.txt", "r")

input = file.readline

# import sys 

# input = sys.stdin.readline

# sys.setrecursionlimit(10**7)

def find(num) : 
	if parent[num] == num : 
		return num
	return find(parent[num])

def union(num, set_num) : 
	if find(num) == num : 
		parent[num] = set_num
		return
	union(parent[num], set_num)

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m) : 
	oper, a, b = map(int, input().split())

	if oper == 1 : 
		print("YES" if a == b or find(a) == find(b) else "NO")
	else : 
		fa, fb = find(a), find(b)
		if a == b or fa == fb : 
			continue 
		elif fa < fb : 
			union(b, fa)
		else : 
			union(a, fb)

# print(parent)


file.close()