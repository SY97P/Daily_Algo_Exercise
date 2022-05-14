def solution(item) : 
	exp = item[0]
	queue = []
	num = ""
	for st in exp : 
		if st.isdigit() : 
			num += st
		else : 
			queue.append(num)
			queue.append(st)
			num = ""
	queue.append(num)
	
	answer, branket = 0, 0
	is_branket = False
	is_first = False
	while queue : 
		curr = queue.pop(0)
		print("curr : ", curr)
		if curr == "-" : 
			is_first = not is_first
			is_branket = True
		if curr != "-" and curr != "+" : 
			if is_branket : 
				branket += int(curr)
			else : 
				if not is_first : 
					if branket == 0 : 
						answer = int(curr)
					else : 
						answer -= branket
						branket = int(curr)
				
			print("answer : ", answer, " branket : ", branket)
		
	answer -= branket 
	print(answer)
	return answer



# 백준 제출용
# exp = input().strip('\n')
					

def main() : 
	tc = []
	file = open("./백준_그리디/잃어버린괄호tc.txt", "r")

	for i in range(4) : 
		expression = (file.readline())
		expression = expression.strip('\n')
		answer = int(file.readline())
		tc.append([expression , answer])

	# print(tc)
	
	file.close()

	for item in tc : 
		print("solution : ", solution(item), " answer : ", item[1])

main()
