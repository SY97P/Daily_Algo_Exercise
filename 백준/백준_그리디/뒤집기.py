def solution(file) :
	for i in range(5) :
		num, answer = file.readline().strip("\n").split()

		# token = "1" if num.count("0") >= num.count("1") else "0"
		item = num[0]
		# print("item : ", item)
		# print("item == 1", item == "1")
		# print("item == 0", item == "0")
		zero_part, one_part = 0 if item == "1" else 1, 1 if item == "1" else 0
		for n in num : 
			if item != n : 
				if item == "0" : zero_part += 1
				else 		: one_part += 1
				item = n
		# print("0 / 1 : ", zero_part, one_part)
		token = "1" if zero_part >= one_part else "0"

		# print(num, token)

		result = 0 
		toggle = False
		for n in num : 
			if n == token : 
				toggle = True
			else : 
				if toggle : 
					result += 1
					toggle = False
			# print(n, result, toggle)
		if toggle : 
			result += 1
		print(result, answer)

# 백준 제출용
num = input().strip('\n')
item = num[0]
zero_part = 0 if item == "1" else 1
one_part = 1 if item == "1" else 0

for n in num : 
	if item != n :
		if item == "0" : zero_part += 1
		else 		   : one_part += 1
token = "1" if zero_part >= one_part else "0"

result = 0
toggle = False
for n in num : 
	if n == token : 
		toggle = True
	else  :
		if toggle : 
			result += 1
			toggle = False
if toggle :
	result += 1
print(result)

def main() : 
	file = open("./백준_그리디/뒤집기tc.txt", "r")

	print("solution : ", solution(file))

	file.close()

main()