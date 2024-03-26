"""
문제요약
- n 개의 숫자
- 중간에 수 변경이 빈번
- 어떤 부분의 합 구하려고 함

제한사항
- N : 수의 개수 (1 <= N <= 1,000,000)
- M : 변경 수 (1 <= M <= 10,000)
- K : 구간 합 수 (1 <= K <= 10,000)
- 그 다음 N 개 숫자 주어짐
- 다음 (a, b, c) 주어짐
    - a = 1 : b번째 수를 c로 바꿈
    - a = 2 : b번째 수부터 c번째 수까지의 합을 구함
- 입력으로 주어지는 숫자는 모두 16 바이트 내에서 커버 가능

해결전략 (세그먼트 트리)
- 세그먼트 트리를 구함
"""
file = open('./구간_합_구하기.txt', 'r')
input = file.readline

from math import ceil, log2


def update(idx, diff) -> None:
    idx += tree_size
    while idx:
        segment_tree[idx] += diff
        idx //= 2


def query(left: int, right: int) -> int:
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

    n, m, k = map(int, input().split())
    nums = [0] + [int(input()) for _ in range(n)]

    h = ceil(log2(len(nums)))
    tree_size = 2 ** (h + 1) - 1
    segment_tree = [0] + [0] * tree_size * 2

    for i, num in enumerate(nums):
        update(i, num)

    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(b, c - nums[b])
        elif a == 2:
            print(query(b, c))


if __name__ == '__main__':
    main()