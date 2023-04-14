n = int(input())
array = list(map(int, input().split()))

answer = -1

l, r = 0, n-1
while l <= r:
	m = (l + r) // 2
	if m == array[m]:
		answer = m
		break
	elif m > array[m]:
		l = m + 1
	else:
		r = m - 1
print(answer)