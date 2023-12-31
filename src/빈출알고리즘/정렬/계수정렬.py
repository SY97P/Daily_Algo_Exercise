array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# * 계수정렬 O(n+k) (k: 데이터 최대값)
# - 데이터의 개수와 최대값이 정해져있을때, 값이 작을때 무척 강력함
# - 데이터가 정수인 경우에만 사용가능(실수 안 됨)
# - 따로 k+1 크기의 리스트를 만들어서 각 정수값의 빈도수를 기록

# * 대안책으로 기수정렬(radix sort)가 있음

count = [0 for i in range(max(array)+1)]

for a in array:
	count[a] += 1

for i, c in enumerate(count):
	if c > 0:
		print(str(i) * c, end=" ")
print()