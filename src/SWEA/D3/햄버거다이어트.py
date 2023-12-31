#1 750	//Test Case #1의 정답

file = open("./SWEA/D3/햄버거다이어트.txt", "r")

input = file.readline

t = int(input())

# index, calorie, score
def dfs(idx, cal, sco) : 
	global score, n, l

	# print(idx, sco, cal)

	for i in range(idx + 1, n) : 
		# ingre[i] = (점수, 칼로리)
		if cal + ingre[i][1] <= l :
			dfs(i, cal + ingre[i][1], sco + ingre[i][0])
		else : 
			# print(sco, score)
			score = max(score, sco)

	score = max(score, sco)
		

for tc in range(1, t + 1) : 
	n, l = map(int, input().split())
	ingre = [tuple(map(int, input().split())) for _ in range(n)]

	# print(n, l)
	# print(ingre)

	score = 0

	for i in range(n) :
		dfs(i, ingre[i][1], ingre[i][0])

	print("#%d %d" % (tc, score))

file.close()