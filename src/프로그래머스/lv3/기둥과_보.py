def is_stable(frame):
    for x, y, a in frame:
        if a == 0:  # 기둥
            if y == 0 or [x, y - 1, 0] in frame or [x - 1, y, 1] in frame or [x, y, 1] in frame:
                continue
            else:
                return False
        elif a == 1:  # 보
            if [x, y - 1, 0] in frame or [x + 1, y - 1, 0] in frame or (
                    [x - 1, y, 1] in frame and [x + 1, y, 1] in frame):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b == 0:  # 삭제
            answer.remove([x, y, a])
            if not is_stable(answer):
                answer.append([x, y, a])
        elif b == 1:  # 설치
            answer.append([x, y, a])
            if not is_stable(answer):
                answer.remove([x, y, a])

    return sorted(answer)


def main():
    expect = [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]
    answer = solution(5,
                      [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                       [3, 2, 1, 1]])
    print(answer, answer == expect)


if __name__ == '__main__':
    main()
