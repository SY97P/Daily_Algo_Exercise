def solution(a, m=1e9, n=1e9):
    l = [m := min(m, x) for x in a]
    r = [n := min(n, x) for x in reversed(a)]
    return sum([(0 if x > y and x > z else 1) for x, y, z in zip(a, l, reversed(r))])


def main():
    # answer = solution([9, -1, -5])  # 3
    answer = solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33])  # 6
    print(answer)


if __name__ == '__main__':
    main()
