# 2

file = open("./Daily_Algo_Exercise/백준/문제집/구현/기차가어둠을헤치고은하수를.txt")

input = file.readline

n, m = map(int, input().split())

train = [0 for _ in range(n)]
shape = [False for _ in range(1 << 22)]
result = 0

for _ in range(m):
	line = list(map(int, input().split()))
	num, i = line[0], line[1] - 1
	x = 0 if len(line) <= 2 else line[2]

	if num == 1:
		train[i] |= 1 << (x - 1)
	elif num == 2:
		train[i] &= ~ (1 << (x - 1))
	elif num == 3:
		train[i] = (train[i] & ~ (1 << 19)) << 1
	else:
		train[i] = (train[i] & ~ (1 << 0)) >> 1

	# for t in train:
	# 	print(bin(t))
	# print()

for t in train:
	if not shape[t]:
		shape[t] = True
		result += 1

print(result)


file.close()