file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/감시피하기.txt")

input = file.readline 


n = int(input())
matrix = [list(input().split()) for _ in range(n)]

answer = False


def check(matrix):
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == "T":
				for k in range(1, n):
					# 동
					if j+k < n:
						if matrix[i][j+k] == "O":
							break
						if matrix[i][j+k] == "S":
							# print("동")
							return False
				for k in range(1, n):
					# 서 
					if j-k >= 0:
						if matrix[i][j-k] == "O":
							break
						if matrix[i][j-k] == "S":
							# print("서")
							return False
				for k in range(1, n):
					# 남
					if i+k < n:
						if matrix[i+k][j] == "O":
							break
						if matrix[i+k][j] == "S":
							# print("남")
							return False
				for k in range(1, n):
					# 북
					if i-k >= 0:
						if matrix[i-k][j] == "O":
							break
						if matrix[i-k][j] == "S":
							# print("북")
							return False
	return True


def dfs(count):
	global answer
	if answer:
		return
	if count == 3:
		answer = answer or check(matrix)
		return 
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == "X":
				matrix[i][j] = "O"
				dfs(count + 1)
				matrix[i][j] = "X"


dfs(0)

print("YES" if answer else "NO")


file.close()