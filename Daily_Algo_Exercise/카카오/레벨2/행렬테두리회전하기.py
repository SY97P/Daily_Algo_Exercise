def solution(rows, cols, queries) :
	answer = 0	# 회전한 애들 중에서 최소인 값

	mat = [[(i+1) + j * rows for i in range(rows)] for j in range(cols)]

	for i in mat : 
		print(i)

	for q in queries : 
		q = [i-1 for i in q]
		temp = mat[q[0]][q[1]]

		for i in range(q[0], q[2]+1) :
			mat[i][q[1]] = mat[i+1][q[1]]
		for i in range(q[1], q[3]+1) : 
			mat[q[2]][i] = mat[q[2]][i+1]
		for i in range(q[2], q[0]-1, -1) : 
			mat[i][q[3]] = mat[i-1][q[3]]
		for i in range(q[3], q[1]-1, -1) : 
			mat[q[0]][i] = mat[q[0]][i-1]
		mat[q[0]][q[1]] = mat[q[0]][q[1]+1]
		mat[q[0]][q[1]+1] = temp

		task = []
		for i in range(q[0], q[2]+1) : 
			task.append(mat[q[1]][i])
			task.append(mat[q[3]][i])
		for i in range(q[1], q[3]+1) : 
			task.append(mat[i][q[0]])
			task.append(mat[i][q[2]])

		print(task)

		for i in mat : 
			print(i)

def main() : 
	rows, cols, queries = 6, 6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]				#[8, 10, 25]
	# rows, cols, queries = 3, 3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	#[1, 1, 5, 3]
	# rows, cols, queries = 100,97,[[1,1,100,97]]								#[1]
	print("solution : ", solution(rows, cols, queries))

main()
