line = input().strip()

word = []
num = 0

for l in line:
	if l.isdigit():
		num += int(l)
	else:
		word.append(l)

word.sort()

answer = ''.join(word) + str(num)

print(answer)