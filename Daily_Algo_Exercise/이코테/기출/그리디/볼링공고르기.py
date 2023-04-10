n, m = map(int, input().split())
array = list(map(int, input().split()))

cnt = [0] * (m+1)
for a in array:
	cnt[a] += 1

answer = 0
rest = n
for c in cnt:
	answer += c * (rest - c)
	rest -= c

print(answer)