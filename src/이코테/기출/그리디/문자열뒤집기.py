number = list(map(int, input().strip()))

count_1 = 0
count_0 = 0

for i in range(len(number)-1):
	if number[i] != number[i+1]:
		if number[i] == 0:
			count_0 += 1
		else:
			count_1 += 1
if number[-1] == 0: count_0 += 1
else: count_1 += 1

print(min(count_0, count_1))