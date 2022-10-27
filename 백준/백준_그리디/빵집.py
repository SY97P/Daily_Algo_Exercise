# 재귀 사용
def solve(matrix, visited, dx, r, c, i, j) :
	# 원웅이네 빵집으로 도착을 했다면 True 반환
	if j == c - 1 :
		# print("[solve] j is approach the column limit")
		return True
	# 아직 원웅이네 빵집이 아니라면 dx별로 갈 수 있는 곳으로 이동
	for d in dx :
		# 확인해야 할 것
		# 1. 범위 내에 있는지
		# 2. '.' 인지 
		# 3. visited False 인지
		# print(0 <= i + d < r and matrix[i+d][j+1] == '.' and not visited[i+d][j+1])
		if 0 <= i + d < r and matrix[i+d][j+1] == '.' and not visited[i+d][j+1] :
			# print("[solve] tuple what applied dx is True")
			visited[i+d][j+1] = True
			if solve(matrix, visited, dx, r, c, i+d, j+1) :
				# print("recursive solve func is starting")
				return True
	return False

def solution(file) :
	for _ in range(2) :
		r, c= map(int, file.readline().split())
		matrix = [list(file.readline().strip('\n')) for _ in range(r)]
		answer = int(file.readline())
		file.readline()

		print(r, c, answer)
		for m in matrix :
			print(m)

		# logic 
		dx = [-1, 0, 1] # [위, 앞, 아래]
		visited = [[False for _ in range(c)] for _ in range(r)]
		count = 0

		for i in range(r) :
			# 첫 스타트가 '.'인 경우에만 로직 순회
			if matrix[i][0] == '.' :
				if not visited[i][0] :
					# print("row number ", i, " is beginning")
					if solve(matrix, visited, dx, r, c, i, 0) :
						count += 1

		print(count)

# 백준 제출용
import sys

def solve(matrix, visited, dx, r, c, i, j) :
	# 원웅이네 빵집으로 도착을 했다면 True 반환
	if j == c - 1 :
		# print("[solve] j is approach the column limit")
		return True
	# 아직 원웅이네 빵집이 아니라면 dx별로 갈 수 있는 곳으로 이동
	for d in dx :
		# 확인해야 할 것
		# 1. 범위 내에 있는지
		# 2. '.' 인지 
		# 3. visited False 인지
		# print(0 <= i + d < r and matrix[i+d][j+1] == '.' and not visited[i+d][j+1])
		if 0 <= i + d < r and matrix[i+d][j+1] == '.' and not visited[i+d][j+1] :
			# print("[solve] tuple what applied dx is True")
			visited[i+d][j+1] = True
			if solve(matrix, visited, dx, r, c, i+d, j+1) :
				# print("recursive solve func is starting")
				return True
	return False

r, c = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().strip('\n'))) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
count = 0
dx = [-1, 0, 1]

for i in range(r) :
	# 첫 스타트가 '.'인 경우에만 로직 순회
	if matrix[i][0] == '.' :
		if not visited[i][0] :
			# print("row number ", i, " is beginning")
			if solve(matrix, visited, dx, r, c, i, 0) :
				count += 1

print(count)


def main() :
	file = open("./백준_그리디/빵집tc.txt")
	print("solution : ", solution(file))
	file.close()

main()

