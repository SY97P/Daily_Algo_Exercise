"""
문제요약

- 시침, 분침, 초침이 있을때 초침과 나머지 두 침이 일치하면 알람 울림
- 특정 시간 동안 알람이 울린 횟수 구하기

제한사항

- 0 <= 시각 <= 23
- 0 <= 분 <= 59
- 0 <= 초 <= 59

해결전략

- 1분에 초침은 시침, 분침과 각각 1번씩 만남
    - 1분에 2회 알람
    - 시간 당 60회 알람
    - 하루에 1440회 알람
- 예외
    - 59분 ~ 00분
        - 해당 시간에는 분침과 만나지 않고, 다음 시 00분에 초침과 분침 만남
        - 즉, 1시간 마다 한 번씩 분침-초침 알람이 생략됨
        - 24시간 기준 24회 알람 생략
    - 11시 ~ 12시 / 23시 ~ 24시
        - 분과 마찬가지로 해당 시간에는 시침-분침 알림 생략됨
        - 24시간 기준 하루에 2회 알람 생략
- (00:00 ~ h2:m2:s2)알람수 - (00:00 ~ h1:m1:s1)알람수 구하기
    - 다만 h1:m1:s1 가 00:00:00 이거나 12:00:00 이면 알람부터 치고 시작 (+1)
    - 초침이 시침 각도나 분침 각도보다 큰 각이라면 알람이 각각 1회씩 울렸을 것
"""


def get_alarm_count(h, m, s):
    count = 0

    s_degree = (s * 6) % 360
    m_degree = (m * 6 + s * 0.1) % 360
    h_degree = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360

    if s_degree >= m_degree:
        count += 1
    if s_degree >= h_degree:
        count += 1

    count += (h * 60 + m) * 2 - h
    if h >= 12:
        count -= 2

    return count


def solution(h1, m1, s1, h2, m2, s2):
    cnt1 = get_alarm_count(h1, m1, s1)
    cnt2 = get_alarm_count(h2, m2, s2)
    answer = cnt2 - cnt1
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        return answer + 1
    return answer


def main():
    # 2
    answer = solution(0, 5, 30, 0, 7, 0)
    print(answer)

    # 1
    answer = solution(12, 0, 0, 12, 0, 30)
    print(answer)

    # 0
    answer = solution(0, 6, 1, 0, 6, 6)
    print(answer)

    # 1
    answer = solution(11, 59, 30, 12, 0, 0)
    print(answer)

    # 1
    answer = solution(11, 58, 59, 11, 59, 0)
    print(answer)

    # 2
    answer = solution(1, 5, 5, 1, 5, 6)
    print(answer)

    # 2852
    answer = solution(0, 0, 0, 23, 59, 59)
    print(answer)


if __name__ == '__main__':
    main()
