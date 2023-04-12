def check(word):
	count = 0
	for w in word:
		if w == "(":
			count += 1
		else:
			if count == 0:
				return False
			count -= 1
	return True

def split_word(word):
	count = 0
	idx = 0
	for i, w in enumerate(word):
		if w == "(":
			count += 1
		else:
			count -= 1
		if count == 0:
			idx = i
			break
	return word[:idx+1], word[idx+1:]

def concat(word):
	result = ""
	for i in range(1, len(word)-1):
		if word[i] == "(":
			result += ")"
		else:
			result += "("
	return result

def solution(line):
	if len(line) == 0:
		return ""
	u, v = split_word(line)

	answer = ""

	if check(u):
		answer = u + solution(v)
	else:
		answer = "(" + solution(v) + ")" + concat(u)
	return answer

line = input().strip()
print(solution(line))