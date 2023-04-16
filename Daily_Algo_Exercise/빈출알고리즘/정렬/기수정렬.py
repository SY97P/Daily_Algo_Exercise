# * 기수정렬 O(d * (n+b))
# - 안정적 정렬
# - d: 최대 자릿수(10의 배수의 개수)
# - n: 정렬할 데이터 수
# - b: bucket의 크기(기수정렬의 경우 10으로 고정: 0~9)
# - 장점
# 	1. 문자열, 정수 정렬이 가능
# 	2. 자릿수가 고정되어 있어서 안정적
# - 단점
# 	1. 자릿수가 없는 경우 정렬 불가 (부동소수점)
# 	2. bucket 추가 공간 필요

from collections import deque

def radix_sort(arr):
	bucket = [deque() for _ in range(10)]

	max_val = max(arr)
	q = deque(arr)
	curr_digit = 1

	while max_val >= curr_digit:
		while q:
			num = q.popleft()
			bucket[(num//curr_digit)%10].append(num)
		for i in range(10):
			while bucket[i]:
				q.append(bucket[i].popleft())
		curr_digit *= 10

	return list(q)

def main():
	arr = [4, 5, 2, 2, 8, 1, 3]
	answer = radix_sort(arr)
	print(answer)

main()