s = "aabbaccc"
s = "ababcdcdababcdcd"

result = []

for step in range(1, len(s)):
	count = 1
	crypt = ""
	token = s[:step]
	for i in range(step, len(s), step):
		tok = s[i:i+step]
		if token == tok:
			count += 1
		else:
			if count > 1:
				crypt += str(count) + token
			else:
				crypt += token
			token = tok
			count = 1
	if count > 1:
		crypt += str(count) + token
	else:
		crypt += token
	print(step, crypt)
	result.append(crypt)

answer = len(s)
for r in result:
	if len(r) < answer:
		answer = len(r)

print(answer)
	