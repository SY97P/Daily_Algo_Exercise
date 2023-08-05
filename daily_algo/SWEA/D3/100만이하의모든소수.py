num = 10 ** 6

visited = [False, False] + [True] * (num - 1)

for i in range(2, int(num ** 0.5)) :
	# 현재 숫자가 소수라면
	# 소수에서 만들어지는 곱수는 모두 제거
	if visited[i] :
		for j in range(2 * i, num + 1, i) :
			visited[j] = False

# prime = []

for idx, v in enumerate(visited) : 
	if v : 
		# prime.append(idx)
		print(idx, end = " ")
