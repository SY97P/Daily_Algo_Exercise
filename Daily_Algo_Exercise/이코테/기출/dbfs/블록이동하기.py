from collections import deque

def get_pos(board, pos):
	result = []
	(x1, y1), (x2, y2) = pos
	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	for dx, dy in d:
		nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
		if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
			result.append({(nx1, ny1), (nx2, ny2)})
	if x1 == x2:
		for k in [1, -1]:
			if board[x1+k][y1] == 0 and board[x2+k][y2] == 0:
				result.append({(x1, y1), (x1+k, y1)})
				result.append({(x2, y2), (x2+k, y2)})
	else:
		for k in [1, -1]:
			if board[x1][y1+k] == 0 and board[x2][y2+k] == 0:
				result.append({(x1, y1), (x1, y1+k)})
				result.append({(x2, y2), (x2, y2+k)})
	return result

def solution(board):
	n = len(board)
	new_board = [[1] * (n+2) for _ in range(n+2)]
	for i in range(n):
		for j in range(n):
			new_board[i+1][j+1] = board[i][j]
	
	pos = {(1, 1), (1, 2)}
	visited = [pos]
	
	q = deque([(0, pos)])

	answer = 0

	while q:
		cnt, pos = list(q.popleft())

		if (n, n) in pos:
			answer = cnt
			break 

		for next_pos in get_pos(new_board, pos):
			if next_pos not in visited:
				visited.append(next_pos)
				q.append((cnt + 1, next_pos))

	return answer

def main():
	board = [[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
	print(solution(board))

main()