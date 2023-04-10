array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# * 삽입정렬 O(n^2)
# - 현재 기준 왼쪽으로는 리스트가 정렬되어 있다고 가정
# - 따라서 1번 인덱스부터 연산 시작
# - 정렬할 현재 인덱스 기준 왼쪽 값이 나보다 크면 스왑
# - 해당 인덱스에 정렬할 값 넣기

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
		else:
			break

print(array)