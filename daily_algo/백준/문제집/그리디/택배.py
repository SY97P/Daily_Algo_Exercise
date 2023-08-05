# 70
# 150

file = open("./Daily_Algo_Exercise/백준/문제집/그리디/택배.txt")

input = file.readline 

for _ in range(2):
	n, c = map(int, input().split())
	m = int(input())
	data = [tuple(map(int, input().split())) for _ in range(m)]
	data.sort(key=lambda x: (x[1], x[0], x[2]))
	
	for d in data:
		print(d)
	
	cap = [c for _ in range(n)]
	result = 0
	for s, e, w in data:
		min_c = min(c, w)
		for i in range(s, e):
			if min_c > cap[i]:
				min_c = cap[i]
		for i in range(s, e):
			cap[i] -= min_c
		result += min_c
				
	print(result)

file.close()