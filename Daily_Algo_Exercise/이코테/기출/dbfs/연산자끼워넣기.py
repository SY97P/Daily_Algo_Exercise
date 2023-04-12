file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/연산자끼워넣기.txt")

input = file.readline 


from collections import deque

n = int(input())
array = list(map(int, input().split()))
oper = list(map(int, input().split()))
min_val, max_val = int(1e9), -int(1e9)

def dfs(idx, val, oper):
	global min_val, max_val
	if idx == n-1:
		min_val = min(min_val, val)
		max_val = max(max_val, val)
		return
	for i in range(4):
		if oper[i] > 0:
			oper[i] -= 1
			next_val = val
			if i == 0:
				next_val += array[idx+1]
			elif i == 1:
				next_val -= array[idx+1]
			elif i == 2:
				next_val *= array[idx+1]
			elif i == 3:
				next_val = next_val // array[idx+1] if next_val >= 0 else -(-next_val // array[idx+1])
			dfs(idx+1, next_val, oper)
			oper[i] += 1
	

dfs(0, array[0], oper)

print(max_val)
print(min_val)


file.close()