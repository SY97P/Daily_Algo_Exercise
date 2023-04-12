import bisect

n, x = map(int, input().split())
array = list(map(int, input().split()))

left_bound = bisect.bisect_left(array, x)
right_bound = bisect.bisect_right(array, x)

print(right_bound - left_bound if right_bound-left_bound != 0 else -1)

# n, x = map(int, input().split())
# array = list(map(int, input().split()))

# left_bound, right_bound = 0, 0

# l, r = 0, n-1
# while l <= r:
# 	m = (l + r) // 2
# 	if x <= array[m]:
# 		left_bound = m
# 		r = m - 1
# 	else:
# 		l = m + 1

# l, r = 0, n-1
# while l <= r:
# 	m = (l + r) // 2
# 	if x >= array[m]:
# 		right_bound = m
# 		l = m + 1
# 	else:
# 		r = m - 1

# answer = right_bound - left_bound + 1
# print(answer if answer != n else -1)