file = open("./그리디/폴리오미노tc.txt", "r")

pol = ["AAAA", "BB"]

def poliomino(index) : 
	global format
	if index + 4 <= length and "." not in format[index:index+4] :
		# AAAA가 와도 되는 타이밍
		format = format[:index] + pol[0] + format[index+4:]
		return 4
	elif index + 2 <= length and "." not in format[index:index+2] :
		# BB 가 와도 되는 타이밍
		format = format[:index] + pol[1] + format[index+2:]
		return 2
	else : 
		# 어림 없지
		return -1
		

for tc in range(5) :
	format = file.readline().strip("\n")
	answer = file.readline().strip("\n")
	file.readline()

	print(tc + 1, "번째 test case")
	print(format)
	print(answer)

	index = 0
	length = len(format)
	# print(index, length)

	while index < length : 
		# print("index : ", index)
		if format[index] == "." :
			index += 1
			continue
		pol_value = poliomino(index)
		if pol_value != -1 :
			index += pol_value
		else :
			format = -1
			break

	print(format)
	print()

file.close()

# 백준 제출용
# pol = ["AAAA", "BB"]

# def poliomino(index) :
# 	global format
# 	if index + 4 <= length and "." not in format[index:index+4] :
# 		format = format[:index] + pol[0] + format[index+4:]
# 		return 4
# 	elif index + 2 <= length and "." not in format[index:index+2] :
# 		format = format[:index] + pol[1] + format[index+2:]
# 	else :
# 		return -1

# format = input().strip("\n")

# index, length = 0, len(format)

# while index < length :
# 	if format[index] == "." :
# 		index += 1
# 		continue
# 	pol_value = poliomino(index)
# 	if pol_value != -1 : 
# 		index += pol_value
# 	else :
# 		format = -1
# 		break
# print(format)