"""
문제요약

- 탑승 중엔 항상 (최저기준온도) ~ (최대기준온도) 온도 유지
- 온도 변화
    - 에어컨 켜면 실내온도 -> 희망온도
    - 에어컨 끄면 실내온도 -> 실외온도
- 전력 소비
    - 희망온도 != 실내온도 : a
    - 희망온도 == 실내온도 : b
    - 에어컨 끄기 : 0
- 조건에 모두 부합하며 최소로 소모한 전력 구하기

제한사항

- -10 <= 실외온도 <= 40
- -10 <= 최저기준온도 < 최대기준온도 < 40
- 실외온도는 기준온도 바깥 범위 값
- 1 <= a, b <= 100
- 2 <= onboard 길이 <= 1_000
    - onboard[i] = 1 : 탑승 중
    - onboard[0] = 0 : 미탑승
    - 무조건 한 번은 승객이 탑승함

해결전략 (DP)

- 온도 초기값 변화
    - 배열로 영하온도 처리하기 위해 최저온도인 -10 만큼 모든 온도값에 더해줌
- 최저, 최대 온도 구하기
    - 승객이 탑승 중일때는 [t1, t2] 구간만 결과에 영향
    - 승객 미탑승 중에는 [min(t1, 실외), max(t2, 실외)] 구간만 결과에 영향
- DP
    - dp[i][j] : i 시간에 j 온도를 맞추기 위한 최소전력
    - 이전온도 < 현재온도
        - 이전온도 < 실외온도 -> 에어컨 꺼도 현재온도 됨 (0)
        - 이전온도 > 실외온도 -> 에어컨 켜야 현재온도 됨 (a)
    - 이전온도 = 현재온도
        - 이전온도 = 실외온도 -> 에어컨 꺼도 현재온도 됨 (0)
        - 이전온도 != 실외온도 -> 에어컨 켜야 현재온도 됨 (b)
            - 이전온도와 희망온도(현재온도)가 같음
    - 이전온도 > 현재온도
        - 이전온도 < 실외온도 -> 에어컨 켜야 현재온도 됨 (a)
        - 이전온도 > 실외온도 -> 에어컨 꺼도 현재온도 됨 (0)
"""


def solution(temperature, t1, t2, a, b, onboard):
    temperature, t1, t2 = temperature + 11, t1 + 11 , t2 + 11
    min_t, max_t = min(t1, temperature), max(t2, temperature)
    dp = [[1e9] * 53 for _ in range(len(onboard))]
    dp[0][temperature] = 0

    for i in range(1, len(onboard)):
        (start, end) = (t1, t2) if onboard[i] else (min_t, max_t)
        for j in range(start, end + 1):
            low = dp[i - 1][j - 1] + (0 if j - 1 < temperature else a)
            same = dp[i - 1][j] + (0 if j == temperature else b)
            high = dp[i - 1][j + 1] + (0 if j + 1 > temperature else a)

            dp[i][j] = min(dp[i][j], low, same, high)

    return min(dp[-1])


def main():
    # 40
    answer = solution(28, 18, 26, 10, 8, [0, 0, 1, 1, 1, 1, 1])
    print(answer)

    # 25
    answer = solution(-10, -5, 5, 5, 1, [0, 0, 0, 0, 0, 1, 0])
    print(answer)

    # 20
    answer = solution(11, 8, 10, 10, 1, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1])
    print(answer)

    # 60
    answer = solution(11, 8, 10, 10, 100, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1])
    print(answer)


if __name__ == '__main__':
    main()