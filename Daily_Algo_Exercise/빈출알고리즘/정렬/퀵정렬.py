array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# * 퀵정렬 O(n log n)
# - 데이터가 거의 정렬되어있지 않을때 강력함.
# - 피벗: list[0], 테일: list[1:]
# - 1번 방법, left: 피벗보다 작은 값들, right: 피벗보다 큰 값들 -> 분할정복(원소 개수가 1일 때 종료)
# - 2번 방법, left: 왼쪽부터 피벗보다 큰 값 위치, right: 오른쪽부터 피벗보다 작은 값 위치
# 	-> 둘이 엇갈리면 피벗위치와 right을 스왑
# 	-> 엇갈리지 않으면 left, right 서로 스왑

def quick_sort_2(array, start, end):
	if start >= end:
		return

	pivot = start
	left, right = start + 1, end
	while left <= right:
		while left <= end and array[pivot] >= array[left]:
			left += 1
		while right > start and array[pivot] <= array[right]:
			right -= 1
		if left > right:
			array[pivot], array[right] = array[right], array[pivot]
		else:
			array[left], array[right] = array[right], array[left]
	quick_sort_2(array, start, right-1)
	quick_sort_2(array, right+1, end)

def quick_sort_1(array):
	if len(array) <= 1:
		return array

	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return quick_sort_1(left_side) + [pivot] + quick_sort_1(right_side)


print(quick_sort_1(array))
quick_sort_2(array, 0, len(array)-1)
print(array)