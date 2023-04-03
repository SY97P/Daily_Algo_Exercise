# 1 4 5 3 2

file = open("./Daily_Algo_Exercise/백준/문제집/구현/원상복구_small.txt")

input = file.readline

n, k = map(int, input().split())
slist = list(map(int, input().split()))
dlist = list(map(int, input().split()))

plist = [0 for _ in range(n + 1)]

for _ in range(k):
	for i in range(n):
		plist[dlist[i]] = slist[i]
	slist = plist[1:]

print(* plist[1:])

file.close()