number = list(map(int, input().strip()))

answer = number[0]

for i in range(1, len(number)):
	if answer not in (0, 1) and number[i] not in (0, 1):
		answer *= number[i]
	else:
		answer += number[i]

print(answer)