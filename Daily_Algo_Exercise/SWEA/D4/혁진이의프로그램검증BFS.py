#1 YES
#2 NO
#3 YES
#4 YES
#5 YES
#6 YES
#7 NO
#8 NO
#9 YES
#10 YES
#11 YES
#12 YES
#13 YES
#14 NO
#15 YES
#16 YES
#17 YES
#18 YES
#19 YES
#20 YES
#21 YES
#22 YES
#23 YES
#24 YES
#25 YES
#26 YES
#27 YES
#28 YES
#29 YES
#30 YES
#31 YES
#32 YES
#33 YES
#34 YES
#35 NO
#36 YES
#37 YES
#38 YES
#39 NO
#40 NO
#41 YES
#42 YES
#43 NO
#44 YES
#45 YES
#46 YES
#47 YES
#48 NO
#49 NO
#50 YES
#51 NO
#52 YES
#53 YES
#54 YES
#55 YES
#56 YES
#57 NO
#58 YES
#59 YES
#60 NO
#61 YES
#62 YES
#63 NO
#64 YES
#65 YES
#66 YES
#67 YES
#68 YES
#69 YES

file = open("./SWEA/D4/혁진이의프로그램검증.txt", "r")

input = file.readline

from collections import deque

t = int(input())

def move(comm, i, j) : 
	global r, c
	
	if comm == "<" : 
		j -= 1
		if j < 0 : 
			j = c - 1
	elif comm == ">" :
		j += 1
		if j >= c : 
			j = 0
	elif comm == "v" : 
		i += 1
		if i >= r : 
			i = 0
	elif comm == "^" : 
		i -= 1
		if i < 0 : 
			i = r - 1
	else :
		print("cannot be : ", comm)
	return (comm, i, j)


def mem_move(comm, i, j, mem) : 
	if mem == 0 : 
		if comm == "_" : 
			dir, di, dj = move(">", i, j)
		else: 
			dir, di, dj = move("v", i, j)
	else : 
		if comm == "_" :
			dir, di, dj = move("<", i, j)
		else : 
			dir, di, dj = move("^", i, j)

	return (dir, di, dj)


def bfs(r, c) : 
	temp = [[0 for _ in range(c)] for _ in range(r)]
	temp[0][0] = 1
	q = deque([(0, 0,">", 0, temp)])

	termin = False

	while q :
		i, j, dir, mem, visited = q.popleft()
		comm = lines[i][j]

		# print(i, j, dir, "/ mem : ", mem, " comm : ", comm, visited[i][j])

		if comm == "@" : 
			termin = True
			break
		elif comm in set(["_", "|"]) :
			ddir, di, dj = mem_move(comm, i, j, mem)
		elif comm == "?" :
			for d in ["v", "^", ">", "<"] : 
				ddir, di, dj = move(d, i, j)
				if lines[di][dj] == "@" : 
					termin = True
					break
				if visited[di][dj] < 2 : 
					visited[di][dj] += 1
					q.append((di, dj, ddir, mem, visited))
			continue
		elif comm == "." : 
			ddir, di, dj = move(dir, i, j)
		elif 48 <= ord(comm) < 58 :
			ddir, di, dj = move(dir, i, j)
			mem = int(comm)
		elif comm == "+" : 
			ddir, di, dj = move(dir, i, j)
			mem = mem + 1 if mem < 15 else 0
		elif comm == "-" : 
			ddir, di, dj = move(dir, i, j)
			mem = mem - 1 if mem > 0 else 15
		else : 
			ddir, di, dj = move(comm, i, j)
			if (comm == ">" and lines[di][dj] == "<") or (comm == "<" and lines[di][dj] == ">") or (comm == "^" and lines[di][dj] == "v") or (comm == "v" and lines[di][dj] == "^"): 
				continue
		
		if lines[di][dj] == "@" : 
			termin = True
			break
		if visited[di][dj] < 20 :
			visited[di][dj] += 1
			q.append((di, dj, ddir, mem, visited))

	return termin

for tc in range(1, t + 1) : 
	r, c = map(int, input().split())
	lines = [list(input().strip()) for _ in range(r)]

	# if tc != 69 : 
	# 	continue

	# print(r, c)
	# for l in lines :
	# 	print(l)

	if bfs(r, c) :
		print("#%d YES" % tc)
	else : 
		print("#%d NO" % tc)

file.close()