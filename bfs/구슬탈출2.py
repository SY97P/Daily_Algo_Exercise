# 해결방안 1번 :
# BFS
# 예외처리
# 1. R, B가 같은 줄에서 같은 방향으로 움직일 때 겹치지 않도록 제어
# 2. R, B 모두 움직이지 않았다면 count 증가되지 않도록 해야 함.
# 3. 상하좌우 순서이기 때문에 오른쪽 방향을 먼저 고려했으면 답을 구할 수 있는 문제를 놓침
# 4. 공이 동시에 빠진다는 건 한 턴에 빠진다는 이야기였음. 이에 대한 처리 필요
#  -> 리스트에 -1 있으면 -> -1 / 1이랑 0만 -> 1 / 0만 -> 0
# 5. 10 넘어가는 건 계산하지 않음
from collections import deque

file = open("./bfs/구슬탈출2tc.txt", "r")

def validate(lst) : 
	print(lst)
	if -1 in lst : 
		return -1
	elif 1 in lst : 
		return 1
	else : 
		return 0

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
		tr, tb, count, rvisited, bvisited = queue.popleft()
		
		dic = dict()

		print("ri, rj, bi, bj, count : ", tr, tb, count)

		if count > 10 :
			print("종료조건!!")
			return -1

		# print(ri, rj, bi, bj)

		# 4방향으로 갔을 때 도달할 수 있는 좌표를 넣어줌
		# 상하좌우 순서
		# 상
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		code_list = []
		while 0 < ri < n-1 and 0 <= bi < n-1:
			if matrix[ri-1][rj] != '#' :
				ri -= 1
			else : 
				red_stop = True
			if matrix[bi-1][bj] != '#' :
				bi -= 1
			else :
				blue_stop = True
			code = checkin((ri, rj), (bi, bj))
			code_list.append(code)
			# 예외3번 : 방향에 우선순위 없음
			# if code == 1 : 
			# 	return count + 1
			# elif code == 0 :
			if red_stop and blue_stop :
				# 예외1번 : 겹치는 지 확인
				# 겹치면 원래 위치와의 거리를 계산해서 더 많이 움직인 쪽을 진행방향에서 한 칸 모자라게 수정
				if ri == bi and rj == bj :
					# 더 많이 움직인 쪽
					if abs(tr[0] - ri) > abs(tb[0] - bi) : # r이 많이
						# r을 한 칸 덜 움직이게 함
						ri += 1
					else : 
						bi += 1
				break
			# else : 
			# 	return -1
		# not 둘다 방문한 게 아니라면 -> 둘 중 하나라도 방문하지 않았다면
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			# 예외2 : 둘 다 움직이지 않았을 때 count 증가
			if (ri, rj) != tr or (bi, bj) != tb :
				print("상 - ri, rj, bi, bj, count + 1 : ", ri, rj, bi, bj, count + 1)
				# 예외3번 : 방향 가능성 넣는 타이밍 조정
				# queue.append(((ri, rj), (bi, bj), count + 1))
				# dic에 넣어서 관리할 예정
				rvisited[ri][rj] = bvisited[bi][bj] = True
				dic["상"] = ((ri, rj), (bi, bj), count + 1, validate(code_list), rvisited, bvisited)
				rvisited[ri][rj] = bvisited[bi][bj] = False
			

		# 하
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		code_list = []
		while 0 < ri < n-1 and 0 < bi < n-1:
			if  matrix[ri+1][rj] != '#' :
				ri += 1
			else : 
				red_stop = True
			if matrix[bi+1][bj] != '#' :
				bi += 1
			else : 
				blue_stop = True
			code = checkin((ri, rj), (bi, bj))
			code_list.append(code)
			# print("하 ri,code : ", code)
			# if code == 1 : 
			# 	return count + 1
			# elif code == 0 :
			if red_stop and blue_stop :
				if ri == bi and rj == bj : 
					if abs(tr[0] - ri) > abs(tb[0] - bi) :
						ri -= 1
					else : 
						bi -= 1
				break
			# else : 
			# 	return -1
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			if (ri, rj) != tr or (bi, bj) != tb :
				print("하 - ri, rj, bi, bj, count + 1 : ", ri, rj, bi, bj, count + 1)
				# queue.append(((ri, rj), (bi, bj), count + 1))
				
				rvisited[ri][rj] = bvisited[bi][bj] = True
				dic["하"] = ((ri, rj), (bi, bj), count + 1, validate(code_list), rvisited, bvisited)
				rvisited[ri][rj] = bvisited[bi][bj] = False

		# 좌
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		code_list = []
		while 0 < rj < m-1 and 0 < bj < m-1 :
			if matrix[ri][rj-1] != '#' :
				rj -= 1
			else : 
				red_stop = True
			if matrix[bi][bj-1] != '#' :
				bj -= 1
			else : 
				blue_stop = True
			code = checkin((ri, rj), (bi, bj))
			code_list.append(code)
			# print("좌 code : ", code)
			# if code == 1 : 
			# 	return count + 1
			# elif code == 0 :
			if red_stop and blue_stop :
				if ri == bi and rj == bj :
					if abs(tr[1] - rj) > abs(tb[1] - bj) :
						rj += 1
					else :
						bj += 1
				break
			# else : 
			# 	print("here?")
			# 	return -1
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			if (ri, rj) != tr or (bi, bj) != tb :
				print("좌 - ri, rj, bi, bj, count + 1 : ", ri, rj, bi, bj, count + 1)
				# queue.append(((ri, rj), (bi, bj), count + 1))
				
				rvisited[ri][rj] = bvisited[bi][bj] = True
				dic["좌"] = ((ri, rj), (bi, bj), count + 1, validate(code_list), rvisited, bvisited)
				rvisited[ri][rj] = bvisited[bi][bj] = False

		# 우
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		code_list = []
		while 0 < rj < m-1 and 0 < bj < m-1 :
			if matrix[ri][rj+1] != '#' :
				rj += 1
			else : 
				red_stop = True
			if matrix[bi][bj+1] != '#' :
				bj += 1
			else :
				blue_stop = True
			code = checkin((ri, rj), (bi, bj))
			code_list.append(code)
			# print("우 code : ", code)
			# if code == 1 : 
			# 	return count + 1
			# elif code == 0 :
			if red_stop and blue_stop :
				if ri == bi and rj == bj :
					if abs(tr[1] - rj) > abs(tb[1] - bj) : 
						rj -= 1
					else :
						bj -= 1
				break
			# else : 
			# 	return -1
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			if (ri, rj) != tr or (bi, bj) != tb :
				print("우 - ri, rj, bi, bj, count + 1 : ", ri, rj, bi, bj, count + 1)
				# queue.append(((ri, rj), (bi, bj), count + 1))
				
				rvisited[ri][rj] = bvisited[bi][bj] = True
				dic["우"] = ((ri, rj), (bi, bj), count + 1, validate(code_list), rvisited, bvisited)
				rvisited[ri][rj] = bvisited[bi][bj] = False

		# 예외3번 : 여기서 다음 큐에 들어갈 요소를 구분해서 넣어야 함. 
		# 각 방향에 대한 정보를 dic으로 모아왔으니 순회하면서 넣으면 됨
		# code 1 -> return data[2] / code 0 -> append / code -1 -> no append
		for value in dic.values() :
			rd, bd, cd, code, rvisited, bvisited = value
			# 예외5번 : count 가 10 넘어가는 건 계산하지 않음
			if cd <= 10 : 
				if code == 1 : 
					return cd
				elif code == 0 :
					queue.append((rd, bd, cd, rvisited, bvisited))
	return -1	
		

answer_list = []
result_list = []
for tc in range(13) : 
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
	answer_list.append(answer)
	file.readline()

	# if tc not in [4, 6] :
	# 	continue

	print(n, m, answer)
	print("ri, rj, bi, bj, hole_i, hole_j : ", ri, rj,"/", bi, bj,"/", hole_i, hole_j)
	for mat in matrix : 
		print(mat)

	rvisited = [[False for _ in range(m)] for _ in range(n)]
	bvisited = [[False for _ in range(m)] for _ in range(n)]
	rvisited[ri][rj] = bvisited[bi][bj] = True
	result = bfs(deque([((ri, rj), (bi, bj), 0, rvisited, bvisited)]))
	print(result)
	result_list.append(result)

	print()

for i in range(len(answer_list)) : 
	print("answer , result : ", answer_list[i], result_list[i])

file.close()


# 백준 제출용
# 해결방안 1번 :
# BFS
# 예외처리
# 1. R, B가 같은 줄에서 같은 방향으로 움직일 때 겹치지 않도록 제어
# 2. R, B 모두 움직이지 않았다면 count 증가되지 않도록 해야 함.
# 3. 상하좌우 순서이기 때문에 오른쪽 방향을 먼저 고려했으면 답을 구할 수 있는 문제를 놓침
# 4. 공이 동시에 빠진다는 건 한 턴에 빠진다는 이야기였음. 이에 대한 처리 필요
#  -> 리스트에 -1 있으면 -> -1 / 1이랑 0만 -> 1 / 0만 -> 0
# 5. 10 넘어가는 건 계산하지 않음
from collections import deque
from sys import stdin

def validate(lst) : 
	# print(lst)
	if -1 in lst : 
		return -1
	elif 1 in lst : 
		return 1
	else : 
		return 0

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
		tr, tb, count, rvisited, bvisited = queue.popleft()
		
		dic = dict()

		# print("ri, rj, bi, bj, count : ", tr, tb, count)

		if count > 10 :
			# print("종료조건!!")
			return -1

		# print(ri, rj, bi, bj)

		# 4방향으로 갔을 때 도달할 수 있는 좌표를 넣어줌
		# 상하좌우 순서
		# 상
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		code_list = []
		
		while 0 < ri < n-1 and 0 <= bi < n-1:
			if matrix[ri-1][rj] != '#' :
				ri -= 1
			else : 
				red_stop = True
			if matrix[bi-1][bj] != '#' :
				bi -= 1
			else :
				blue_stop = True
				
			code = checkin((ri, rj), (bi, bj))
			code_list.append(code)
			
			# 예외3번 : 방향에 우선순위 없음
			# if code == 1 : 
			# 	return count + 1
			# elif code == 0 :
			
			if red_stop and blue_stop :
				# 예외1번 : 겹치는 지 확인
				# 겹치면 원래 위치와의 거리를 계산해서 더 많이 움직인 쪽을 진행방향에서 한 칸 모자라게 수정
				if ri == bi and rj == bj :
					# 더 많이 움직인 쪽
					if abs(tr[0] - ri) > abs(tb[0] - bi) : # r이 많이
						# r을 한 칸 덜 움직이게 함
						ri += 1
					else : 
						bi += 1
				break
			# else : 
			# 	return -1
				
		# not 둘다 방문한 게 아니라면 -> 둘 중 하나라도 방문하지 않았다면
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			# 예외2 : 둘 다 움직이지 않았을 때 count 증가
			if (ri, rj) != tr or (bi, bj) != tb :
				# print("상 - ri, rj, bi, bj, count + 1 : ", ri, rj, bi, bj, count + 1)
				# 예외3번 : 방향 가능성 넣는 타이밍 조정
				# queue.append(((ri, rj), (bi, bj), count + 1))
				# dic에 넣어서 관리할 예정
				rvisited[ri][rj] = bvisited[bi][bj] = True
				dic["상"] = ((ri, rj), (bi, bj), count + 1, validate(code_list), rvisited, bvisited)
				rvisited[ri][rj] = bvisited[bi][bj] = False
			

		# 하
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		code_list = []
		
		while 0 < ri < n-1 and 0 < bi < n-1:
			if  matrix[ri+1][rj] != '#' :
				ri += 1
			else : 
				red_stop = True
			if matrix[bi+1][bj] != '#' :
				bi += 1
			else : 
				blue_stop = True
				
			code = checkin((ri, rj), (bi, bj))
			code_list.append(code)
			
			# print("하 ri,code : ", code)
			# if code == 1 : 
			# 	return count + 1
			# elif code == 0 :
			
			if red_stop and blue_stop :
				if ri == bi and rj == bj : 
					if abs(tr[0] - ri) > abs(tb[0] - bi) :
						ri -= 1
					else : 
						bi -= 1
				break
				
			# else : 
			# 	return -1
				
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			if (ri, rj) != tr or (bi, bj) != tb :
				# print("하 - ri, rj, bi, bj, count + 1 : ", ri, rj, bi, bj, count + 1)
				# queue.append(((ri, rj), (bi, bj), count + 1))
				
				rvisited[ri][rj] = bvisited[bi][bj] = True
				dic["하"] = ((ri, rj), (bi, bj), count + 1, validate(code_list), rvisited, bvisited)
				rvisited[ri][rj] = bvisited[bi][bj] = False

		# 좌
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		code_list = []
		
		while 0 < rj < m-1 and 0 < bj < m-1 :
			if matrix[ri][rj-1] != '#' :
				rj -= 1
			else : 
				red_stop = True
				
			if matrix[bi][bj-1] != '#' :
				bj -= 1
			else : 
				blue_stop = True
				
			code = checkin((ri, rj), (bi, bj))
			code_list.append(code)
			
			# print("좌 code : ", code)
			# if code == 1 : 
			# 	return count + 1
			# elif code == 0 :
			
			if red_stop and blue_stop :
				if ri == bi and rj == bj :
					if abs(tr[1] - rj) > abs(tb[1] - bj) :
						rj += 1
					else :
						bj += 1
				break
				
			# else : 
			# 	print("here?")
			# 	return -1
				
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			if (ri, rj) != tr or (bi, bj) != tb :
				# print("좌 - ri, rj, bi, bj, count + 1 : ", ri, rj, bi, bj, count + 1)
				# queue.append(((ri, rj), (bi, bj), count + 1))
				
				rvisited[ri][rj] = bvisited[bi][bj] = True
				dic["좌"] = ((ri, rj), (bi, bj), count + 1, validate(code_list), rvisited, bvisited)
				rvisited[ri][rj] = bvisited[bi][bj] = False

		# 우
		red_stop, blue_stop = False, False
		(ri, rj), (bi, bj) = tr, tb
		code_list = []
		
		while 0 < rj < m-1 and 0 < bj < m-1 :
			if matrix[ri][rj+1] != '#' :
				rj += 1
			else : 
				red_stop = True
				
			if matrix[bi][bj+1] != '#' :
				bj += 1
			else :
				blue_stop = True
				
			code = checkin((ri, rj), (bi, bj))
			code_list.append(code)
			
			# print("우 code : ", code)
			# if code == 1 : 
			# 	return count + 1
			# elif code == 0 :
			
			if red_stop and blue_stop :
				if ri == bi and rj == bj :
					if abs(tr[1] - rj) > abs(tb[1] - bj) : 
						rj -= 1
					else :
						bj -= 1
				break
			# else : 
			# 	return -1
				
		if not(rvisited[ri][rj] and bvisited[bi][bj]) :
			if (ri, rj) != tr or (bi, bj) != tb :
				# print("우 - ri, rj, bi, bj, count + 1 : ", ri, rj, bi, bj, count + 1)
				# queue.append(((ri, rj), (bi, bj), count + 1))
				
				rvisited[ri][rj] = bvisited[bi][bj] = True
				dic["우"] = ((ri, rj), (bi, bj), count + 1, validate(code_list), rvisited, bvisited)
				rvisited[ri][rj] = bvisited[bi][bj] = False

		# 예외3번 : 여기서 다음 큐에 들어갈 요소를 구분해서 넣어야 함. 
		# 각 방향에 대한 정보를 dic으로 모아왔으니 순회하면서 넣으면 됨
		# code 1 -> return data[2] / code 0 -> append / code -1 -> no append
		for value in dic.values() :
			rd, bd, cd, code, rvisited, bvisited = value
          # 예외5번 : count가 10 넘어가는 건 계산하지 않음
			if cd <= 10 : 
				if code == 1 : 
					return cd
				elif code == 0 :
					queue.append((rd, bd, cd, rvisited, bvisited))
	return -1	
		
n, m = map(int, stdin.readline().split())
hole_i = hole_j = 0
ri = rj = bi = bj = 0
matrix = []
for i in range(n) : 
	line = list(stdin.readline().strip("\n"))
	for j, li in enumerate(line) : 
		if li == 'O' :
			hole_i, hole_j = i, j
		if li == 'R' :
			ri, rj = i, j
		if li == 'B' :
			bi, bj = i, j
	matrix.append(line)

rvisited = [[False for _ in range(m)] for _ in range(n)]
bvisited = [[False for _ in range(m)] for _ in range(n)]
rvisited[ri][rj] = bvisited[bi][bj] = True
result = bfs(deque([((ri, rj), (bi, bj), 0, rvisited, bvisited)]))
print(result)