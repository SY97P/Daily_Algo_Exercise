# 300
# 864

# Knuth's Algorithm 사용한 버전
# python3로는 시간초과 / pypy3 로는 통과

file = open("./백준/dp/lv2/파일합치기.txt", "r")

input = file.readline

t = int(input())

def mergeFiles(n, sum_list) :
	for i in range(2, n + 1) : 
		for j in range(1, n + 2 - i) : 
			dp[j][j-1+i] = min([dp[j][k] + dp[k+1][j-1+i] for k in range(j, j-1+i)]) + (sum_list[j-1+i] - sum_list[j-1])

	# for d in dp : 
	# 	print(d)

	return dp[1][-1]

def getAccuSum() :
	sum_list = [0 for _ in range(n + 1)]

	for i in range(1, n + 1) : 
		sum_list[i] = sum_list[i-1] + files[i]

	# print(sum_list)

	return sum_list
			

for _ in range(t) : 
	n = int(input())

	files = [0] + list(map(int, input().split()))

	dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

	sum_list = getAccuSum()

	print(mergeFiles(n, sum_list))


file.close()