# n, c = 5, 3
# array = [1,2,8,4,9]

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]

array.sort()

answer = 0

l, r = 1, array[-1] + 1
while l <= r:
	m = (l + r) // 2
	count = 1
	curr = array[0] + m
	for i in range(1, n):
		if curr <= array[i]:
			count += 1
			curr = array[i] + m
	# print(m, count)
	if count < c:
		r = m - 1
	else:
		answer = m
		l = m + 1
print(answer)