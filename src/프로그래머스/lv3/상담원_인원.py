"""
문제요약

- 멘토 n 명
- 1 ~ k 상담유형
- 각 멘토는 상담유형 중 하나만 담당
- 멘토는 동시에 참가자 한 명과만 상담 가능
- 상담 시간은 참가자 요청 시간만큼 소요
- 각 유형별로 멘토 한 명 이상
- 참가자 기다린 시간이 최소가 되도록 상담 유형별 멘토 인원 구하기

- 규칙
    - 참가자 상담 요청 시 해당 상담 유형 멘토 중 idle 멘토가 상담 시작
    - 모든 멘토가 상담 중이면, 해당 유형 멘토가 유휴일때까지 기다렸다가 상담
    - 참가자 기다린 시간 = 멘토 상담 시작 - 상담 요청 시간
    - 해당 유형 참가자 중에 가장 먼저 요청 참가자가 우선해서 상담

제한사항

- 1 <= 상담 유형 <= 5
- 상담유형 <= 멘토 수 <= 20
- 3 <= 참가자 수 <= 300
- req = [상담요청시각, 상담소요시간, 상담유형] -> 상담요청시각 기준 오름차순 정렬
- 1 <= 상담요청시각(중복없음) <= 1_000
- 1 <= 상담소요시간 <= 100

해결전략

조합
- 각 유형 별로 인원수 달리해서 적용해보기
- 모든 유형별 인원 배정으로 총 기다린 시간 구하기
- 그 중에서 최소인 시간 구하기

"""
from itertools import product


def get_time(clist, reqs):
    time = 0

    for k in range(len(clist)):
        mentos = [0] * clist[k]
        for a, b, c in reqs:
            c -= 1
            if c == k:
                min_time = min(mentos)
                if min_time > a:
                    time += min(mentos) - a
                    for i in range(clist[k]):
                        if min_time == mentos[i]:
                            mentos[i] += b
                            break
                else:
                    for i in range(clist[k]):
                        if min_time == mentos[i]:
                            mentos[i] = a + b
                            break

    return time


def solution(k, n, reqs):
    answer = 1e9
    clist = product(range(1, n + 1), repeat=k)
    for c in clist:
        if sum(c) != n:
            continue
        answer = min(answer, get_time(c, reqs))

    return answer


def main():
    # 25
    answer = solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]])
    print(answer)

    # 90
    answer = solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]])
    print(answer)


if __name__ == '__main__':
    main()
