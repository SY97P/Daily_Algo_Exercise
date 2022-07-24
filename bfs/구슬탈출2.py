# 해결방안 1번 :
# BFS

from collections import deque

file = open("./bfs/구슬탈출2tc.txt", "r")

def checkin(r, b) :
	red_in, blue_in = False, False
	
	if matrix[r[0]][r[1]] == 'O' :
		red_in = True
	if matrix[b[0]][b[1]] == 'O' :
		blue_in = True

	if red_in and not blue_in :
		return 1
	elif not red_in and not blue_in :
		return 0
	else :
		return -1


def bfs(queue) : 
	global hole_i
	global hole_j

	while queue : 
		tr, tb, count = queue.popleft()

		print("ri, rj, bi, bj, count : ", tr, tb, count)

		if count > 10 :
			return -1

		# print(ri, rj, bi, bj)

		# 4방향으로 갔을 때 도달할 수 있는 좌표를 넣어줌
		# 상하좌우 순서
		# 상
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		while 0 < ri < n-1 :
			if matrix[ri-1][rj] != '#' :
				ri -= 1
			else : 
				red_stop = True
			if matrix[bi-1][bj] != '#' :
				bi -= 1
			else :
				blue_stop = True
			code = checkin((ri, rj), (bi, bj))
			print("상 ri, rj, bi, bj, code : ",ri, rj, "/", bi, bj, "/", code)
			if code == 1 : 
				return count + 1
			elif code == 0 :
				if red_stop and blue_stop :
					break
				continue
			else : 
				return -1
		# not 둘다 방문한 게 아니라면 -> 둘 중 하나라도 방문하지 않았다면
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			queue.append(((ri, rj), (bi, bj), count + 1))

		# 하
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		while 0 < ri < n-1 :
			if  matrix[ri+1][rj] != '#' :
				ri += 1
			else : 
				red_stop = True
			if matrix[bi+1][bj] != '#' :
				bi += 1
			else : 
				blue_stop = True
			code = checkin((ri, rj), (bi, bj))
			print("하 code : ", code)
			if code == 1 : 
				return count + 1
			elif code == 0 :
				if red_stop and blue_stop :
					break
				continue
			else : 
				return -1
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			queue.append(((ri, rj), (bi, bj), count + 1))

		# 좌
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		while 0 < rj < m-1 :
			if matrix[ri][rj-1] != '#' :
				rj -= 1
			else : 
				red_stop = True
			if matrix[bi][bj-1] != '#' :
				bj -= 1
			else : 
				blue_stop = True
			code = checkin((ri, rj), (bi, bj))
			print("좌 code : ", code)
			if code == 1 : 
				return count + 1
			elif code == 0 :
				if red_stop and blue_stop :
					break
				continue
			else : 
				return -1
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			queue.append(((ri, rj), (bi, bj), count + 1))

		# 우
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		while 0 < rj < m-1 :
			if matrix[ri][rj+1] != '#' :
				rj += 1
			else : 
				red_stop = True
			if matrix[bi][bj+1] != '#' :
				bj += 1
			else :
				blue_stop = True
			code = checkin((ri, rj), (bi, bj))
			print("우 code : ", code)
			if code == 1 : 
				return count + 1
			elif code == 0 :
				if red_stop and blue_stop :
					break
				continue
			else : 
				return -1
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			queue.append(((ri, rj), (bi, bj), count + 1))
		
		

for tc in range(7) : 
	n, m = map(int, file.readline().split())
	hole_i = hole_j = 0
	ri = rj = bi = bj = 0
	matrix = []
	for i in range(n) : 
		line = list(file.readline().strip("\n"))
		for j, li in enumerate(line) : 
			if li == 'O' :
				hole_i, hole_j = i, j
			if li == 'R' :
				ri, rj = i, j
			if li == 'B' :
				bi, bj = i, j
		matrix.append(line)
				
	answer = int(file.readline())
	file.readline()

	if tc != 1 :
		continue

	print(n, m, answer)
	print("ri, rj, bi, bj, hole_i, hole_j : ", ri, rj,"/", bi, bj,"/", hole_i, hole_j)
	for mat in matrix : 
		print(mat)

	rvisited = [[False for _ in range(m)] for _ in range(n)]
	bvisited = [[False for _ in range(m)] for _ in range(n)]
	result = bfs(deque([((ri, rj), (bi, bj), 0)]))
	print(result)

	print()

file.close()