# 54
# 1053

file = open("./Daily_Algo_Exercise/백준/문제집/구현/상어초등학교.txt")

input = file.readline

n = int(input())
info = []
dic = dict()
for _ in range(n**2):
	num, a, b, c, d = map(int, input().split())
	info.append((num, (a, b, c, d)))
	dic[num] = (a, b, c, d)

mat = [[0 for _ in range(n)] for _ in range(n)]
mat[(n-1)//2][(n-1)//2] = info[0][0]

# for inf in info:
# 	print(inf)
# for key in dic.keys():
# 	print(key, dic[key])

# print()
# for m in mat:
# 	print(m)

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

result = 0

for k in range(1, n**2):
	num, fav = info[k]
	x, y = 0, 0
	fav_count = -1
	emp_count = -1
	for i in range(n):
		for j in range(n):
			if mat[i][j] == 0:
				fav_temp = 0 
				emp_temp = 0
				for dx, dy in d:
					di = i + dx
					dj = j + dy
					if 0 <= di < n and 0 <= dj < n:
						if mat[di][dj] in fav:
							fav_temp += 1
						if mat[di][dj] == 0:
							emp_temp += 1
				if fav_temp > fav_count or (fav_temp == fav_count and emp_temp > emp_count):
					fav_count = fav_temp
					if emp_temp >= emp_count:
						emp_count = emp_temp
						x, y = i, j
	mat[x][y] = num

# print()
# for m in mat:
# 	print(m)

result = 0
for i in range(n):
	for j in range(n):
		count = 0
		for dx, dy in d:
			di = i + dx
			dj = j + dy
			if 0 <= di < n and 0 <= dj < n and mat[di][dj] in dic[mat[i][j]]:
				count += 1
		if count <= 1:
			result += count
		elif count == 2:
			result += 10
		elif count == 3:
			result += 100
		else:
			result += 1000
print(result)


file.close()