file = open("./백준_그리디/A와Btc.txt", "r")

def operation(mode) :
	global temp

	if mode == 0 :
		temp += "A"
	else :
		lst = list(temp)
		lst.reverse()
		lst += "B"

def reverse_operation(mode) : 
	global temp

	if mode == 0 : 
		temp = temp[:len(temp)-1]
	else : 
		temp = temp[:len(temp)-1]
		lst = list(temp)
		lst.reverse()
		temp = ''.join(lst)

for _ in range(2) : 
	s = file.readline().strip("\n")
	t = file.readline().strip("\n")
	answer = int(file.readline())
	file.readline()

	print(s, t, answer)

	temp = t
	possible = True

	# 문제에서는 s를 t로 만들라고 했지만
	# 나는 t에서 s를 만들 수 있는지 확인할 것
	while temp != s : 
		# temp길이가 s보다 작아지면 종료
		if len(temp) < len(s) : 
			possible = False
			break
		if temp[-1] == "A" :
			reverse_operation(0)
		else : 
			reverse_operation(1)

	if possible :
		print(1)
	else : 
		print(0)
	print()

file.close()

# 백준 제출용
s = input().strip("\n")
t = input().strip("\n")

def reverse_operation(mode) : 
	global temp

	if mode == 0 : 
		temp = temp[:len(temp)-1]
	else : 
		temp = temp[:len(temp)-1]
		lst = list(temp)
		lst.reverse()
		temp = ''.join(lst)


temp = t
possible = True

# 문제에서는 s를 t로 만들라고 했지만
# 나는 t에서 s를 만들 수 있는지 확인할 것
while temp != s : 
	# temp길이가 s보다 작아지면 종료
	if len(temp) < len(s) : 
		possible = False
		break
	if temp[-1] == "A" :
		reverse_operation(0)
	else : 
		reverse_operation(1)

if possible :
	print(1)
else : 
	print(0)