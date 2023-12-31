#1 12345 52341
#2 14325 54321
#3 124857 842157
#4 10000 10000

file = open("./SWEA/D3/숫자조작.txt", "r")

input = file.readline

import copy

t = int(input())

def modify(numm, i, j) : 
	num = copy.deepcopy(numm)
	temp = num[i]
	num[i] = num[j]
	num[j] = temp
	return int(''.join(map(str, num)))

for tc in range(1, t + 1) : 
	num_origin = int(input())
	num_list = list(map(int, str(num_origin)))
	length = len(num_list)

	min_result = max_result = num_origin 

	for i in range(length - 1) : 
		min_value = num_list[i]
		min_index = 0
		for j in range(length-1, i, -1) : 
			if min_value > num_list[j] :
				if i == 0  and num_list[j] == 0 : 
					continue
				min_value = num_list[j]
				min_index = j
		if min_value != num_list[i] : 
			min_result = modify(num_list, i, min_index)
			break

	for i in range(length - 1) : 
		max_value = num_list[i]
		max_index = 0
		for j in range(length-1, i, -1) : 
			if max_value < num_list[j] :
				if i == 0 and num_list[j] == 0 : 
					continue
				max_value = num_list[j]
				max_index = j
		if max_value != num_list[i] : 
			max_result = modify(num_list, i, max_index)
			break

	print("#%d %d %d" %(tc, min_result, max_result))

file.close()