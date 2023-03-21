# w(1, 1, 1) = 2
# w(2, 2, 2) = 4
# w(10, 4, 6) = 523
# w(50, 50, 50) = 1048576
# w(-1, 7, 18) = 1

file = open("./백준/dp/신나는함수실행.txt", "r")

input = file.readline

def w(a, b, c) : 
	if dp[a][b][c] != 0 :
		return dp[a][b][c]
	elif a < b and b < c :
		dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
	else :
		dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

	return dp[a][b][c]

while True : 
	a, b, c = map(int, input().split())

	if a == -1 and b == -1 and c == -1 : 
		break 
	
	print("w(%d, %d, %d) = " %(a, b, c), end = "")
		
	if a <= 0 or b <= 0 or c <= 0 : 
		print(1)
	else : 
		if a > 20 or b > 20 or c > 20 : 
			a, b, c = 20, 20, 20
		dp = [[[0 for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]

		for i in range(a + 1) : 
			for j in range(b + 1) : 
				for k in range(c + 1) :
					if i == 0 or j == 0 or k == 0 : 
						dp[i][j][k] = 1
		w(a, b, c)
		print(dp[a][b][c])

file.close()