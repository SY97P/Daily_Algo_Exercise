file = open("./이진탐색/가장긴증가하는부분수열2tc.txt", "r")

for _ in range(3) : 
	n = int(file.readline())
	nlist = list(map(int, file.readline().split()))
	answer = int(file.readline())
	file.readline()

	print(n, answer)
	print(nlist)

	dp = [1 for _ in range(n)]

	for i, nl in enumerate(nlist) :
		for j in range(i) :
			if nl > nlist[j] : 
				dp[i] = max(dp[i], dp[j] + 1)

	print(dp)
	print(max(dp))

file.close()
