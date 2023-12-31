def solution(s) : 
	answer = 0
	length = len(s)
	lst = []

	for k in range(1, length // 2 + 1) : 
		tokens = []
		for i in range(0, len(s), k) : 
			tokens.append(s[i:i+k])
		# print(tokens)
		candi = ""
		count = 1
		for j in range(len(tokens)-1) : 
			if tokens[j] == tokens[j+1] : 
				count += 1
			else : 
				candi += str(count) + tokens[j] if count > 1 else tokens[j]
				count = 1
		candi += str(count) + tokens[len(tokens)-1] if count > 1 else tokens[len(tokens)-1]
		# print(candi)
		lst.append(len(candi))

	# print(lst)
	return min(lst) if lst else 1
		
	

def main() : 
	s = "aabbaccc"					# 7
	s = "ababcdcdababcdcd"			# 9
	s = "abcabcdede"				# 8
	s = "abcabcabcabcdededededede"	# 14
	s = "xababcdcdababcdcd"			# 17
	s = "xaaaa"						# 3 (x4a)
	s = "xababa"						# 5 (xa2ba)
	s = "x"					
	print("solution : ", solution(s))

main()