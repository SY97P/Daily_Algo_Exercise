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

t = int(input())

def mem_move(comm, i, j, mem) :
	if mem == 0 : 
		if comm == "_" : 
			return move(">", i, j)
		elif comm == "|" :
			return move("v", i, j)
	else : 
		if comm == "_" : 
			return move("<", i, j)
		elif comm == "|" :
			return move("^", i, j)
			

def move(comm, i, j) : 
	global r, c

	dir = 0
	
	if comm == "<" :
		dir = 1
		j -= 1
		if j < 0 : 
			j = c - 1
	elif comm == ">" :
		dir = 0
		j += 1
		if j == c : 
			j = 0
	elif comm == "^" :
		dir = 3
		i -= 1
		if i < 0 : 
			i = r - 1
	elif comm == "v" :
		dir = 2
		i += 1
		if i == r : 
			i = 0
	return (dir, i, j)

def move_dir(dir, i, j) : 
	if dir == 0 : 
		_, di, dj = move(">", i, j)
	elif dir == 1 : 
		_, di, dj = move("<", i, j)
	elif dir == 2 : 
		_, di, dj = move("v", i, j)
	else : 
		_, di, dj = move("^", i, j)
	return (dir, di, dj)
	
def dfs(i, j, dir, mem) : 
	global r, c, terminate

	curr = lines[i][j]
	visited[i][j] += 1

	# print(i, j, dir, curr, mem, visited[i][j])

	if visited[i][j] > 10 ** 2 :
		# print("recursion limit occured")
		return

	if curr == "@" : 
		terminate = True
		return
	elif curr == "." :
		_, di, dj = move_dir(dir, i, j)
		dfs(di, dj, dir, mem)
	elif curr in values :
		_, di, dj = move_dir(dir, i, j)
		dfs(di, dj, dir, int(lines[i][j]))
	elif curr == "+" :
		_, di, dj = move_dir(dir, i, j)
		dfs(di, dj, dir, mem + 1 if mem < 15 else 0)
	elif curr == "-":
		_, di, dj = move_dir(dir, i, j)
		dfs(di, dj, dir, mem - 1 if mem > 0 else 15)
	elif curr == "?" : 
		for d in range(4) : 
			_, di, dj = move_dir(d, i, j)
			if visited[di][dj] < 1 :
				dfs(di, dj, d, mem)
	elif curr in {"_", "|"} :
		dir, di, dj = mem_move(curr, i, j, mem)
		dfs(di, dj, dir, mem)
	else : 
		ddir, di, dj = move(curr, i, j)
		# print(di, dj)
		if (curr == "<" and lines[di][dj] == ">") or (curr == ">" and lines[di][dj] == "<") :
			pass
		else :
			dfs(di, dj, ddir, mem)

	visited[i][j] -= 1

for tc in range(1, t + 1) : 
	r, c = map(int, input().split())
	lines = [list(input()) for _ in range(r)]

	if tc != 69 : 
		continue

	# print(r, c)
	# for l in lines : 
	# 	print(l)

	contradiction = True

	end_point = []

	# no end_point contradiction
	for i, li in enumerate(lines) : 
		for j, l in enumerate(li) : 
			if "@" == l : 
				contradiction = False
				end_point.append((i, j))

	# # volt near end_point contradiction
	# pattern = [["v", "<", "^", ">"],["^", ">", "v", "<"]]
	# for i, j in end_point :
	# 	near = [lines[i][j+1]
		
		
	if contradiction : 
		print("#%d NO" % tc)
	else :
		mem = 0
		values = {str(i) for i in range(10)}
	
		visited = [[0 for _ in range(c)] for _ in range(r)]
		visited[0][0] = 1
	
		terminate = False
	
		# dir
		# 0 : east
		# 1 : west
		# 2 : south
		# 3 : north
		try : 
			dfs(0, 0, 0, 0)
		except :
			print("hell")
	
		if terminate : 
			print("#%d YES" % (tc))
		else: 
			print("#%d NO" % (tc))

file.close()