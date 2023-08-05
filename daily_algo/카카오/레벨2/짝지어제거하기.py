def solution(s) : 
	answer = 0  # 안 되면 0, 모두 제거 가능하면 1

	stack = []

	for i in s : 
		if not stack : 
			stack.append(i)
		elif stack[-1] == i : 
			stack.pop()
		elif stack[-1] != i : 
			stack.append(i)

	if stack : 
		return 0
	return 1
				
		
def main() : 
	s = "baabaa"	# 1
	# s = "cdcd"	# 0
	s = "bb"		# 1
	s = "bbb"		# 1
	s = "bbbb"
	s = "bbbbb"
	s = "aababba"
	# s = "bababababa" * 100000
	# s = "a"
	print("solution : ", solution(s))

main()


# def solution(s) :
# 	if len(s) % 2 == 1: 
# 		return 0
# 	patterns = cycle([chr(i) * 2 for i in range(97, 123)])
# 	while s : 
# 		if len(s) == 1 : 
# 			return 0
# 		s.remove(next(patterns))