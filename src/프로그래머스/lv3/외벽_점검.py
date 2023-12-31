from itertools import permutations


def solution(n, weak, dist):
    answer = 1e9
    length = len(weak)
    weak += [w + n for w in weak]

    for start in range(length):
        for friends in permutations(dist, len(dist)):
            cnt = 1
            position = weak[start] + friends[cnt - 1]
            for idx in range(length):
                if position < weak[start + idx]:
                    if cnt >= len(dist):
                        if idx < length:
                            cnt = 1e9
                        break
                    position = weak[start + idx] + friends[cnt]
                    cnt += 1
            answer = min(answer, cnt)

    return -1 if answer > len(dist) else answer


def main():
    answer = solution(12, [1, 5, 6, 10], [1, 2, 3, 4])  # 2
    answer = solution(6, [1, 2, 4, 5], [1, 1]) # 2
    print(answer)


if __name__ == '__main__':
    main()
