def solution(n) : 
	answer = ""

	while n > 3 : 
		if n % 3 == 0 : 
			answer = "3" + answer
			n = n//3 - 1
		else : 
			answer = str(n%3) + answer
			n = n//3
	answer =  str(n) + answer
	# print(answer)

	return answer.replace("3", "4")

def main() : 
	n = 1	# 1
	n = 2	# 2
	n = 3	# 4
	n = 4	# 11
	n = 5	# 12
	n = 7	# 21
	
	print("solution : ", solution(n))

main()
