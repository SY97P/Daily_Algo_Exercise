# * 합병정렬
# - 빠른정렬
# - 안정적 정렬 : 같은 값인 경우 원래 순서 유지
# - 균등분할(분할정복)
# - 영역을 쪼갤 수 있는 만큼 쪼갠 후 정렬

# 1. 구간을 (l, m), (m+1, r)로 계속 쪼갬
# 2. l >= m 인 구간이 되면 쪼개기 그만(원소가 한 개가 될 때임)
# 3. merge(합병) 수행 (이 과정에서 정렬 이뤄짐)

def merge_sort(arr, l, r):
	if l < r:
		m = (l+r) // 2
		merge_sort(arr, l, m)
		merge_sort(arr, m+1, r)
		merge(arr, l, m, r)

def merge(arr, l, m, r):
	left = arr[l:m+1]
	right = arr[m+1:r+1]
	i, j, k = 0, 0, l
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	# 나머지 부분
	while i < len(left):
		arr[k] = left[i]
		k += 1
		i += 1
	while j < len(right):
		arr[k] = right[j]
		k += 1
		j += 1

def main():
	arr = [4, 2, 6, 7, 1, 8]
	merge_sort(arr, 0, len(arr)-1)
	print(arr)

main()