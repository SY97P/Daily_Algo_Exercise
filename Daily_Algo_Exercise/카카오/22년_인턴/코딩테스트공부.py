# problems = [needed algo, needed coding, upper algo, upper coding, cost]
def solution(alp, cop, problems) :
	max_alp, max_cop = 0, 0
	for prob in problems :
		max_alp = max(max_alp, prob[0])
		max_cop = max(max_cop, prob[1])

	alp = min(alp, max_alp)
	cop = min(cop, max_cop)
	INF = float('inf')
	dp = [[INF for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
	dp[alp][cop] = 0

	for i in range(alp, max_alp + 1) :
		for j in range(cop, max_cop + 1) :
			if i + 1 <= max_alp :
				dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
			if j + 1 <= max_cop :
				dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

			for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems : 
				if i >= alp_req and j >= cop_req : 
					next_alp, next_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
					dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

	for d in dp :
		print(d)
		
	return dp[-1][-1]

tc = [
	# 15
	[10, 10, [[10,15,2,1,2],[20,20,3,3,4]]],
	# 13
	[0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]]
]

for case in tc : 
	alp, cop, problems = case

	print(case)
	print(solution(alp, cop, problems))
	print()