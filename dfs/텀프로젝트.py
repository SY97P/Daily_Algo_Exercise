
file = open("./dfs/텀프로젝트tc.txt","r")

result = []
tcs = int(file.readline())
for tc in range(tcs) :
	n = int(file.readline())
	choices = [-1] + list(map(int, file.readline().split()))

	print(tc + 1, "번째 TC")
	print(n, choices)

	def dfs(num) :
		global cycle_key
		global not_team

		print(num)

		is_cycle = False
		
		# 나 자신을 선택함
		if num == choices[num] :
			is_team[num] = 1
			cycle_key = num
			print("select himself")
		# 나 자신이 아닌 것을 선택함.
		else : 
			# 사이클 확인 선행
			if num in path :
				# cycle_key = num
				is_cycle = True
				print("cycle occur")
			else : 
				# dfs를 진행하되, 갈 곳이 0이어야 만 감
				if is_team[choices[num]] == 0 :
					path.add(num)
					print("dfs going")
					dfs(choices[num])
				else : 
					not_team = True

		# 사이클 발생
		# 현재 num이 cycle_key와 겹치게 되는 구간까지 팀원 처리
		print(num , is_team[num])
		
		if is_team[num] == 0 :
			is_team[num] = -1 if not_team else 1
		if num == cycle_key :
			not_team = True

		if is_cycle : 
			cycle_key = num
			
		print(is_team)
			
				

	is_team = [0 for _ in range(n+1)]
	for number in range(1, n+1) :
		if is_team[number] == 0 : 
			path = set()
			cycle_key = -1
			not_team = False
			dfs(number)

	print(" ", is_team)
	print(n - is_team.count(1))
	result.append(n - is_team.count(1))
	print()
	
file.readline()
print("answer")
for tc in range(tcs) : 
	print(result[tc], int(file.readline()))
print()
	
file.close()


# 백준 제출용

# import sys

# sys.setrecursionlimit(10 ** 9)

# tcs = int(sys.stdin.readline())
# for tc in range(tcs) :
# 	n = int(sys.stdin.readline())
# 	choices = [-1] + list(map(int, sys.stdin.readline().split()))

# 	def dfs(num) :
# 		global cycle_key
# 		global not_team

# 		is_cycle = False
		
# 		# 나 자신을 선택함
# 		if num == choices[num] :
# 			is_team[num] = 1
# 			cycle_key = num
# 		# 나 자신이 아닌 것을 선택함.
# 		else : 
# 			# 사이클 확인 선행
# 			if num in path :
# 				# cycle_key = num
# 				is_cycle = True
# 			else : 
# 				# dfs를 진행하되, 갈 곳이 0이어야 만 감
# 				if is_team[choices[num]] == 0 :
# 					path.add(num)
# 					dfs(choices[num])
# 				else : 
# 					not_team = True

# 		# 사이클 발생
# 		# 현재 num이 cycle_key와 겹치게 되는 구간까지 팀원 처리
# 		if is_team[num] == 0 :
# 			is_team[num] = -1 if not_team else 1
# 		if num == cycle_key :
# 			not_team = True

# 		if is_cycle : 
# 			cycle_key = num
				

# 	is_team = [0 for _ in range(n+1)]
# 	for number in range(1, n+1) :
# 		if is_team[number] == 0 : 
# 			path = set()
# 			cycle_key = -1
# 			not_team = False
# 			dfs(number)

# 	print(n - is_team.count(1))
