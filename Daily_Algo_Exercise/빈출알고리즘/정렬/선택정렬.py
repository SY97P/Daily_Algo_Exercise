array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# * 선택정렬 O(n^2)
# - 데이터가 거의 정렬된 상태일 때 강력함.
# - 현재 기준으로 오른쪽 리스트에서 최소값을 구해서 현재 위치랑 바꿈.
# - 현재 위치는 가장 왼쪽부터 오른쪽으로 이동

for i in range(len(array)):
	min_idx = i
	for j in range(i+1, len(array)):
		if array[j] < array[min_idx]:
			min_idx = j
	array[i], array[min_idx] = array[min_idx], array[i]

print(array)