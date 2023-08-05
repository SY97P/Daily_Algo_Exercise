# 11
# 12
# 5
# 7
# 8
# 7
# 5
# 4

file = open("./Daily_Algo_Exercise/백준/문제집/투포인터/ㅋㅋ루ㅋㅋ.txt")

input = file.readline 

for _ in range(8):
	word = input().strip()
	
	print(word)

	lk, rk = [], []
	count = 0
	for w in word:
		if w == "K":
			count += 1
		else:
			lk.append(count)
	count = 0 
	for i in range(len(word)-1, -1, -1):
		if word[i] == "K":
			count += 1
		else:
			rk.append(count)
	rk.reverse()

	print(lk)
	print(rk)

	result = 0
	l, r = 0, len(rk) - 1
	while (l <= r):
		result = max(result, (r - l + 1) + 2 * min(lk[l], rk[r]))
		if lk[l] < rk[r]:
			l += 1
		else:
			r -= 1
	print(result)
	
file.close()