file = open("./백준_그리디/회의실배정retc.txt", "r")

for tc in range(2) : 
	n = int(file.readline())
	conf = [tuple(map(int, file.readline().split())) for _ in range(n)] 
	answer = int(file.readline())
	file.readline()

	conf.sort(key = lambda x: (x[1], x[0]))
	
	print(n, answer)
	print(conf)

	time, count = 0, 0

	for start, end in conf : 
		if time <= start :
			time = end
			count += 1

	print(time, count)
	print()

file.close()

# 백준 제출용
# import sys

# file = sys.stdin

# n = int(file.readline())
# conf = [tuple(map(int, file.readline().split())) for _ in range(n)] 

# conf.sort(key = lambda x: (x[1], x[0]))

# time, count = 0, 0

# for start, end in conf : 
# 	if time <= start :
# 		time = end
# 		count += 1

# print(count)
