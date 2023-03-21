#1 4

file = open("./SWEA/D3/부분수열의합.txt", "r")

input = file.readline

t = int(input())

def dfs(i, log) :
	global n, k, count
	
	sumof = 0
	for l in log : 
		sumof += seq[l]

	for j in range(i+1, n) :
		if sumof + seq[j] == k : 
			# case.add(log + [j])
			# print(log + [j])
			count += 1
		elif sumof + seq[j] < k :
			dfs(j, log + [j])

for tc in range(1, t + 1) : 
	n, k = map(int, input().split())
	seq = list(map(int, input().split()))

	# case = set()
	count = 0

	for i in range(n) : 
		if seq[i] == k : 
			count += 1
		elif seq[i] < k : 
			dfs(i, [i])

	# print("#%d %d" %(tc, len(case)))
	print("#%d %d" %(tc, count))

file.close()