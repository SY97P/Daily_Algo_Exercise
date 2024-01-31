"""
세그먼트 트리 자료구조

목적
- 특정 구간 결과값 구하는데 사용
- 주어진 쿼리에 대해 빠르게 응답
	a. 특정 구간 누적합 구하기 (구간 별 합 저장해서 쿼리 속도 향상)

특징
- 이진 트리 구조
- 선형 탐색보다 빠름
	- 누적합의 경우 특정 데이터 변경 시 O(N) -> O(logN) or O(NlogN)
- 메모리 많이 필요

구현
- Top-down 방식 (재귀)
	- 낮은 접근성
	- 낮은 성능
	- 좋은 확장성 (Lazy Propagation 에 유리)
- Bottom-up 방식 (반복문)
	- 높은 성능
"""

from math import ceil, log


"""
세그먼트 트리 구현

- left node (coordi : node * 2 / portion : left ~ mid)
- right node (coordi : node * 2 + 1 / portion : mid + 1 ~ right)
- node (coordi : node / portion : left ~ right)
- 3개 좌표를 사용해 범위를 절반씩(이진트리) 분할해 연산하여 각 노드에 저장
- 구간 길이 1인 경우(left == right) 리프노드이므로 재귀 종료
"""
def segment(left, right, idx) -> int:
	if left == right:
		segment_tree[idx] = nums[left]
		return segment_tree[idx]
	mid = (left + right) // 2
	left_segment = segment(left, mid, idx * 2)
	right_segment = segment(mid + 1, right, idx * 2 + 1)
	segment_tree[idx] = left_segment + right_segment
	return segment_tree[idx]


"""
세그먼트 트리 쿼리에 따른 출력

- 세그먼트 트리에서 대부분의 쿼리 = 범위
- 범위 분기
	- 노드 구간을 벗어난 쿼리 -> 0 리턴
	- 노드 구간 완전 포함하는 쿼리 -> 트리 좌표 값 리턴
	- 노드 구간 일부 포함하는 쿼리 -> 좌, 우 노드 재귀 호출
	- 노드 구간 일부 벗어나는 쿼리 -> 좌, 우 노드 재귀 호출하면서 범위 아닌 부분 날리기
- 변수
	- start, end : 현재 노드 포용 범위
	- left, right : 쿼리 범위
"""
def query_sum(start, end, idx, left, right) -> int:
	if start > right or end < left: # 범위 벗어난 경우
		return 0
	if left <= start and end <= right: # 범위 완전 포함하는 경우
		return segment_tree[idx]
	mid = (start + end) // 2
	left_sub_tree = query_sum(start, mid, idx * 2, left, right)
	right_sub_tree = query_sum(mid + 1, end, idx * 2 + 1, left, right)
	return left_sub_tree + right_sub_tree


"""
세그먼트 트리 업데이트

- 재귀
	- 함수 인자로 원래 값과의 차이 넣어줌
	- 루트부터 DFS 하면서 값 업데이트
- 서순
	- 노드 구간에 벗어난 경우 -> 값 리턴
	- 그 외 -> 값 만큼 + 해줌	
"""
def update(start, end, node, idx, val) -> None:
	if start > idx or end < idx:
		return segment_tree[node]
	segment_tree[node] += val
	if start != end:
		mid = (start + end) // 2
		update(start, mid, node * 2, idx, val)
		update(mid + 1, end, node * 2 + 1, idx, val)


def main():
	global segment_tree, nums

	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	h = ceil(log(len(nums), 2))
	tree_size = pow(2, h + 1) - 1

	segment_tree = [0] + [0] * tree_size
	segment(0, len(nums) - 1, 1)

	print("==세그먼트 트리 생성==")
	print(segment_tree)
	print("==세그먼트 트리 쿼리==")
	print("Sum 0 ~ 5 : ", query_sum(0, len(nums) - 1, 1, 0, 5))
	print("==세그먼트 트리 업데이트==")
	update(0, len(nums) - 1, 1, 0, 2)
	print("==세그먼트 트리 쿼리==")
	print("Sum 0 ~ 5 : ", query_sum(0, len(nums) - 1, 1, 0, 5))
	print("==세그먼트 트리 결과==")
	print(segment_tree)


if __name__ == '__main__':
	main()