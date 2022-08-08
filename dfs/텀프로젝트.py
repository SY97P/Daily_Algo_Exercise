file = open("./dfs/텀프로젝트tc.txt","r")

tcs = int(file.readline())
for tc in range(tcs) :
	n = int(file.readline())
	choices = [-1] + list(map(int, file.readline().split()))

	print(tc + 1, "번째 TC")
	print(n, choices)

	def dfs(num) :
		# 나 자신을 선택함
		if num == choices[num] :
			is_team[num] = True
		# 나 자신이 아닌 것을 선택함.
		else : 
			if num in path : 
				for i in range(len(path)-1, -1, -1) : 
					if path[i] == num : 
						is_team[num] = True
						break
					is_team[path[i]] = True
			else :
				path.append(num)
				dfs(choices[num])
			
		return is_team[num]


	is_team = [False for _ in range(n+1)]
	for number in range(1, n+1) :
		if not is_team[number] : 
			path = []
			# print(number)
			dfs(number)

	print(is_team.count(False) - 1)
	
file.readline()
print()
for tc in range(tcs) : 
	print(int(file.readline()))
	
file.close()

# 백준 제출용
