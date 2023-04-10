number = "02984"
# number = "567"

answer = int(number[0])

for i in range(1, len(number)):
	num = int(number[i])
	if answer <= 1 or num <= 1:
		answer += int(number[i])
	else:
		answer *= int(number[i])

print(answer)