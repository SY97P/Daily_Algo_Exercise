file = open("./Daily_Algo_Exercise/이코테/기출/삼성전자/청소년상어.txt")

input = file.readline 


from copy import deepcopy

def move_fish():
	

num_matrix = [[0]*4 for _ in range(4)]
dir_matrix = [[0]*4 for _ in range(4)]

for i in range(4):
	line = list(map(int, input().split()))
	for j in range(0, 7, 2):
		num_matrix[i][j//2] = line[j]
		dir_matrix[i][j//2] = line[j+1]

for num in num_matrix:
	print(num)
print()

for dir in dir_matrix:
	print(dir)
print()


def dfs(si, sj, sumof, num_mat, dir_mat):
	num_matrix = deepcopy(num_mat)
	dir_matrix = deepcopy(dir_mat)
	next_sum = sumof + num_matrix[si][sj]
	num_matrix[si][sj] = 0


dfs(0, 0, 0, num_matrix, dir_matrix)


file.close()