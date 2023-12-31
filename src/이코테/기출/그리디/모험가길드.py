n = int(input())
array = list(map(int, input().split()))
array.sort()

answer = 0 
count = 1
for a in array:
	if a == count:
		answer += 1
		count = 1
	elif count < a:
		count += 1

print(answer)