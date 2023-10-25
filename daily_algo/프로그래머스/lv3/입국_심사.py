def get_cnt(m, times):
    return sum([(m // time) for time in times])


def solution(n, times):
    l, r = 1, max(times) * n
    answer = r

    while l <= r:
        m = (l + r) // 2
        cnt = get_cnt(m, times)
        if cnt >= n:
            answer = m
            r = m - 1
        else:
            l = m + 1

    return int(answer)


def main():
    answer = solution(6, [7, 10])
    answer = solution(2, [10, 6])
    answer = solution(1e9, [2])
    print(answer)


if __name__ == '__main__':
    main()