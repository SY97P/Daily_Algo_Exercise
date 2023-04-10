n, m = map(int, input().split())
array = list(map(int, input().split()))

def bin_search(array, target):
	result = 0
	l, r = 0, max(array)
	while l <= r:
		mid = (l + r) // 2
		total = 0
		for a in array:
			if a > mid:
				total += a - mid

		if total >= m:
			result = mid
			l = mid + 1
		else:
			r = mid - 1
	return result

print(bin_search(array, m))