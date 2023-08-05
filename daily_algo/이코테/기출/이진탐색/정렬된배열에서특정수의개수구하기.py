from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

# n, x = 7, 4
# array = [1,1,2,2,2,2,3]

# x를 삽입할 가장 왼쪽 인덱스
left_bound = bisect_left(array, x)
# x를 삽입할 가장 오른쪽 인덱스
right_bound = bisect_right(array, x)
print(right_bound - left_bound if right_bound - left_bound != 0 else -1)