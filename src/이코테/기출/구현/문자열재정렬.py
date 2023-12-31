word = input().strip()

num = 0
s = []
for w in word:
	if w.isdigit():
		num += int(w)
	else:
		s.append(w)

s.sort()
result = ''.join(s)
if num != 0:
	result += str(num)
print(result)