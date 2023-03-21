#1 5
#2 7
#3 6
#4 3
#5 4
#6 5
#7 9
#8 5
#9 9
#10 3

file = open("./SWEA/D2/패턴마디의길이.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	line = input().strip()

	for i in range(len(line)) :
		pattern = line[:i + 1]

		if pattern == line[i+1:i+1+len(pattern)] :
			break

	print("#%d %d" % (tc, len(pattern)))
		

file.close()