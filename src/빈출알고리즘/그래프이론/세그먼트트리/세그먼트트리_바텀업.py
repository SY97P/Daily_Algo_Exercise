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
def get_tree_size(n) -> int:
    size = 1
    while size < n:
        size *= 2 # size <<= 1
    return size


"""
세그먼트 트리 업데이트

- 바텀업 방식에서는 초기화가 따로 없이, 업데이트로 모두 동작
"""
def update(idx, diff):
    idx += tree_size
    while idx:
        segment_tree[idx] += diff
        idx //= 2


"""
세그먼트 트리 쿼리

"""
def query_sum(left, right):
    ans = 0
    left += tree_size
    right += tree_size
    while left <= right:
        if left % 2 == 1:
            ans += segment_tree[left]
            left += 1
        left //= 2

        if right % 2 == 0:
            ans += segment_tree[right]
            right -= 1
        right //= 2

    return ans


def main():
    global tree_size, segment_tree, nums

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree_size = get_tree_size(len(nums))
    segment_tree = [0] + [0] * tree_size * 2

    print("==세그먼트 트리 생성==")
    for i, num in enumerate(nums):
        update(i, num)
    print("==세그먼트 트리 결과==")
    print(segment_tree)
    print("==세그먼트 트리 쿼리==")
    print('Sum 0 ~ 5 : ', query_sum(0, 5))
    print("==세그먼트 트리 업데이트==")
    update(0, 2)
    print("==세그먼트 트리 쿼리==")
    print('Sum 0 ~ 5 : ', query_sum(0, 5))
    print("==세그먼트 트리 결과==")
    print(segment_tree)


if __name__ == '__main__':
    main()