def solution(N, number):
    if N == number:
        return 1

    dp = [set()] + [{int(str(N) * (i + 1))} for i in range(8)]

    for cnt in range(2, 9):
        for i in range(1, cnt):
            pa, pb = dp[i], dp[cnt - i]
            for a in pa:
                for b in pb:
                    dp[cnt].add(a + b)
                    dp[cnt].add(a - b)
                    dp[cnt].add(a * b)
                    if b != 0:
                        dp[cnt].add(a // b)
        if number in dp[cnt]:
            return cnt

    return -1


def main():
    answer = solution(5, 12)
    print(answer)


if __name__ == '__main__':
    main()
