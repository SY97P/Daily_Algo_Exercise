'''
문제요약

- 한 변의 길이가 1인 정삼각형 2n + 1 개로 윗변 n, 아랫변 길이 n+1 사다리꼴
- tops 배열에 있는 번호에 해당하는 사다리꼴의 윗변 번호에 정삼각형이 올라감
- 정삼각형과 정삼각형 두 개를 붙인 마름모를 이용해서 해당 다각형을 채운다고 할 때
- 빈 타일이 없도록 채우는 경우의 수를 10_007로 나눈 나머지를 구하기

제한사항

- 1 <= n <= 100_000
- tops 길이 = n
- tops[i] = 1 (정삼각형 존재) / 0 (정삼각형 부재)

해결전략 (DP)

dp[i][j] = n이 i이면서 윗변 존재(j)에 따른 경우의 수
dp[1][0] = 3 / dp[1][1] = 4
dp[2][0] = dp[1][0] + 2 / dp[2][1] =
'''

def solution(n, tops):
    answer = 0
    return answer


def main():
    answer = solution(4, [1, 1, 0, 1])
    print(answer)

    answer = solution(2, [0, 1])
    print(answer)

    answer = solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(answer)


if __name__ == '__main__':
    main()