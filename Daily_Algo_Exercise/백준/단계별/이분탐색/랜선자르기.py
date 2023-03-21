# 200

file = open("./백준/이분탐색/랜선자르기.txt", "r")

input = file.readline

def solve() : 
	left, right = 0, sum(wires)

	while left < right : 
		mid = (left + right) // 2

		if mid == 0 : 
			return right
		
		count = 0
		for wire in wires : 
			count += wire // mid

		# 개수가 모자라면 길이를 짧게 해서 여러개 만들기
		if count < n : 
			right = mid
		else : 
			left = mid + 1

	return right - 1

k, n = map(int, input().split())

wires = [int(input()) for _ in range(k)]

print(solve())

file.close()