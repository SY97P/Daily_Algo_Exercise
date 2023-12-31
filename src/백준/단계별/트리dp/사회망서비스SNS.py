# 3

# 3

file = open("./백준/단계별/트리dp/사회망서비스SNS.txt", "r")

input = file.readline

import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def solve(node) : 
	


initValue = 1
n = int(input())
adj = [[] for _ in range(n+1)]
while True:
	line = input().strip()
	if line == "":
		break
	a, b = map(int, line.split())
	adj[a].append(b)
	adj[b].append(a)

dp = [0 for _ in range(n+1)]

visited = initValue
solve(initValue)

print(dp)


file.close()