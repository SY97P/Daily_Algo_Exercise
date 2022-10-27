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
	while queue :
		curr = queue.pop(0)
		# print("curr : ", curr)
		if curr == "-" : 
			is_branket = True
			if branket != 0 : 
				answer -= branket
				branket = 0
				# is_branket = False
		if curr != "-" and curr != "+" : 
			if is_branket :
				branket += int(curr)
			else : 
				answer += int(curr)
		# print("answer : ", answer, " branket : ", branket)
	answer -= branket

	return answer
		

# 백준 제출용
exp = input().strip('\n')
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
while queue :
	curr = queue.pop(0)
	# print("curr : ", curr)
	if curr == "-" : 
		is_branket = True
		if branket != 0 : 
			answer -= branket
			branket = 0
			# is_branket = False
	if curr != "-" and curr != "+" : 
		if is_branket :
			branket += int(curr)
		else : 
			answer += int(curr)
	# print("answer : ", answer, " branket : ", branket)
answer -= branket
print(answer)
					

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
