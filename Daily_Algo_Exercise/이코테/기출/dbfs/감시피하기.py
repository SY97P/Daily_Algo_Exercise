file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/감시피하기.txt")

input = file.readline 

from copy import deepcopy

n = int(input())
matrix = [list(input().split()) for _ in range(n)]

answer = False


def check(matrix):
	temp = deepcopy(matrix)
	
	for i in range(n):
		for j in range(n):
			if temp[i][j] == "T":
				for k in range(1,n):
					if i+k >= n or matrix[i+k][j] == "O":
						break
					if matrix[i+k][j] == "S":
						# print("남쪽 발견")
						return False
				for k in range(1,n):
					if i-k < 0 or matrix[i-k][j] == "O":
						break
					if matrix[i-k][j] == "S":
						# print("북쪽 발견")
						return False
				for k in range(1,n):
					if j+k >= n or matrix[i][j+k] == "O":
						break 
					if matrix[i][j+k] == "S":
						# print("동쪽 발견")
						return False
				for k in range(1,n):
					if j-k < 0 or matrix[i][j-k] == "O":
						break 
					if matrix[i][j-k] == "S":
						# print("서쪽 발견")
						return False
	return True
						

def dfs(count):
	global answer
	if count >= 3:
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