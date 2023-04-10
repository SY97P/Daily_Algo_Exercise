n = 5
array = [2, 3, 1, 2, 2]

array.sort()

answer = 0
count = 0

for a in array:
	count += 1
	if count >= a:
		answer += 1
		count = 0

print(answer)
