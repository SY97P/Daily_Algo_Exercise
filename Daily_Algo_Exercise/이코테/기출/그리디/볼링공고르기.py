n, m = map(int, input().split())
array = list(map(int, input().split()))

answer = 0
for i in range(1, m+1):
	count = array.count(i)
	answer += count * (n-count)
	n -= count
print(answer)