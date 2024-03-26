"""
문제요약

- 6면 주사위 n개
- 번호 별로 나오는 확률 동일
- A가 먼저 n / 2 개의 주사위를 먼저 가지고, 나머지를 B가 가져감
- 각각 가져간 주사위 굴려서 나온 수의 합이 큰 쪽이 승리 (동점이면 무승부)
- A가 승리할 확률이 가장 높기 위해 골라야 하는 오름차순 주사위 번호 배열 구하기
- 정답은 유일한 경우만 주어짐

제한사항

- 2 <= n (2의 배수) <= 10
- 1 <= 주사위 각 면의 값 <= 100

해결전략

압축 이코딩 방식 (dict)
- 조합으로 A가 고를 주사위 번호 구하기
    - A 만 골라도 B 골라짐
- 각 조합별로 구해지는 모든 합 구하기
    - 값 비교를 위해 Counter로 값마다 개수 구하기 (압축 인코딩)
- A 주사위 합 값보다 작은 B 주사위 합 개수를 모두 구해서 조합별 승리횟수 구하기
- 가장 큰 승리횟수를 가진 조합을 반환
"""

from itertools import combinations
from collections import Counter


def add_sums(sums, dice):
    return [s + d for s in sums for d in dice]


def get_sums(numbers, dice):
    sums = [0]
    for number in numbers:
        sums = add_sums(sums, dice[number])
    return Counter(sums)


def solution(dice):
    answer = []
    vic_cnt = 0
    n = len(dice)

    for a_number in combinations(range(n), n // 2):
        a_number = set(a_number)
        b_number = set(range(n)) - a_number

        a_sums = get_sums(a_number, dice)
        b_sums = get_sums(b_number, dice)

        a_vals = sorted(a_sums.keys())
        b_vals = sorted(b_sums.keys())

        cnt = 0
        for a_val in a_vals:
            for b_val in b_vals:
                if a_val <= b_val:
                    break
                cnt += a_sums[a_val] * b_sums[b_val]

        if cnt > vic_cnt:
            vic_cnt = cnt
            answer = a_number

    return [a + 1 for a in answer]


def main():
    # [1, 4]
    answer1 = solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])
    print(answer1)

    # [2]
    answer2 = solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]])
    print(answer2)

    # [1, 3]
    answer3 = solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]])
    print(answer3)


if __name__ == '__main__':
    main()
