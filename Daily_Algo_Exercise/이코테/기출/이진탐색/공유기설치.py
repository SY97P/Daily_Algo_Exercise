n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()

answer = array[-1] - array[0]

l, r = array[1] - array[0], array[-1] - array[0]
while l <= r:
	m = (l + r) // 2
	count = 1
	curr = array[0]
	for i in range(1, n):
		if curr + m <= array[i]:
			curr = array[i]
			count += 1
	# print(count, c, m)
	if count >= c:
		answer = m
		l = m + 1
	else:
		r = m - 1

print(answer)