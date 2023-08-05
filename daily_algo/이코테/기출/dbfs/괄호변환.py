def split_word(word):
	idx = 0
	count = 0
	for i, w in enumerate(word):
		if w == "(":
			count += 1
		else:
			count -= 1
		if count == 0:
			idx = i
			break
	return word[:idx+1], word[idx+1:]


def correct_word(word):
	count = 0
	for w in word:
		if w == "(":
			count += 1
		else:
			count -= 1
		if count < 0:
			return False
	return True


def convert_word(word):
	result = ""
	for i in range(1, len(word)-1):
		result += ")" if word[i] == "(" else "("
	return result


def solution(word):
	if len(word) == 0:
		return word 

	u, v = split_word(word)

	if correct_word(u):
		return u + solution(v)
	else:
		return "(" + solution(v) + ")" + convert_word(u)


def main():
	word = "(()())()"
	word = ")("
	word = "()))((()"
	print(solution(word))

main()