# 1. counter 를 활용해서 개수가 제일 많은 숫자를 우선해서 연산
# 1.1 answer >= 숫자 counter 개수면 trunning
# 2. 해당 숫자가 오직 하나만 있도록 슬라이딩 윈도를 이용해서 부분수열 만들기
# 3. 최종적으로 만들어진 부분수열의 개수를 활용해서 answer 갱신하기

from collections import Counter


def solution(a):
    answer = 0

    for num, cnt in Counter(a).items():
        if answer >= cnt:
            continue
        idx, count = 0, 0
        while idx+1 < len(a):
            if num not in (a[idx], a[idx+1]) or a[idx] == a[idx+1]:
                idx += 1
            else:
                idx += 2
                count += 1
        answer = max(answer, count)

    return answer*2


def main():
    answer = solution([0]) # 0
    # answer = solution([5, 2, 3, 3, 5, 3]) # 4
    # answer = solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]) # 8
    print(answer)


if __name__ == '__main__':
    main()
