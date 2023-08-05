#1 38 
#2 0 
#3 34
#4 28
#5 24
#6 26
#7 36
#8 30
#9 0
#10 34

file = open("./SWEA/D3/단순2진암호코드.txt", "r")

input = file.readline

t = int(input())

dic = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]

for tc in range(1, t + 1) : 
	n, m = map(int, input().split())
	lines = []
	for _ in range(n) : 
		line = input().strip().rstrip("0")
		if line != '' : 
			lines.append(line)

	# if tc != 1 : 
	# 	continue

	code = lines[0]

	crypt = []
	for i in range(len(code), -1, -7) :
		curr = code[i-7:i]
		digit = -1 
		for j in range(10) : 
			if curr == dic[j] : 
				digit = j
				break
		if digit != -1 : 
			crypt.append(digit)
			
	# print(crypt)

	sumof = 0
	for i in range(8) :
		if i % 2 == 0 : 
			sumof += crypt[i]
		else : 
			sumof += crypt[i] * 3

	result = 0
	if sumof % 10 == 0 : 
		result = sum(crypt)

	print("#%d %d" % (tc, result))
	
file.close()
