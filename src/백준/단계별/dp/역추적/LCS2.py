# 4
# ACAK

file = open("./백준/dp/역추적/LCS2.txt", "r")

input = file.readline

import sys

sys.setrecursionlimit(10 ** 9)

def get_lcs_dp() :
	global a, b, len_a, len_b
	
	for i in range(1, len_a + 1) : 
		for j in range(1, len_b + 1) :
			if a[i-1] == b[j-1] : 
				dp[i][j] = dp[i-1][j-1] + 1
			dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i-1][j])

	# for d in dp : 
	# 	print(d)

def tracking(i, j) :
	if dp[i][j] == 0 : 
		return 

	# 좌측 상측 확인
	for dx, dy in d : 
		di = i + dx
		dj = j + dy
		if 0 <= di and 0 <= dj and dp[i][j] == dp[di][dj] : 
			return tracking(di, dj)

	track.append(a[i-1])
	return tracking(i-1, j-1)
	
	

a = input().strip()
b = input().strip()

len_a = len(a)
len_b = len(b)

d = [(0, -1), (-1, 0)]

dp = [[0 for _ in range(len_b + 1)] for _ in range(len_a + 1)]
track = []

get_lcs_dp()

tracking(len_a, len_b)

print(len(track))
if len(track) != 0 : 
	print(''.join(track[::-1]))

file.close()