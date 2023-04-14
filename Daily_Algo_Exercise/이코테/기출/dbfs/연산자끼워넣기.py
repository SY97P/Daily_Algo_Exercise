file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/연산자끼워넣기.txt")

input = file.readline 


n = int(input())
array = list(map(int, input().split()))
oper = list(map(int, input().split()))

result = [-int(1e9), int(1e9)]

def dfs(idx, val, oper):
	if idx >= n-1:
		result[0] = max(result[0], val)
		result[1] = min(result[1], val)
		return

	for i, o in enumerate(oper):
		next_idx = idx + 1
		if o != 0:
			oper[i] -= 1
			if i == 0:
				dfs(next_idx, val + array[next_idx], oper)	
			elif i == 1:
				dfs(next_idx, val - array[next_idx], oper)
			elif i == 2:
				dfs(next_idx, val * array[next_idx], oper)
			elif i == 3:
				next_val = val // array[next_idx]
				if val < 0:
					next_val = -(-val // array[next_idx])
				dfs(next_idx, next_val, oper)
			oper[i] += 1

dfs(0, array[0], oper)

for r in result:
	print(r)


file.close()