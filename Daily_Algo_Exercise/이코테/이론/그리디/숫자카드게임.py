n, m = map(int, input().split())

result = 0

for _ in range(n):
	min_value = min(map(int, input().split()))
	result = max(result, min_value)

print(result)