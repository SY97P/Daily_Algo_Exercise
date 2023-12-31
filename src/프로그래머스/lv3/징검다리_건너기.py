def possible(m, stones, k):
    cnt = 0
    for stone in stones:
        if stone - m < 0:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True


def solution(stones, k):
    answer = 1
    l, r = 1, max(stones)+1
    while l <= r:
        m = int((l + r) // 2)
        if possible(m, stones, k):
            answer = m
            l = m + 1
        else:
            r = m - 1
    return answer

def main():
    # answer = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
    # answer = solution([1, 1, 1], 1)
    # answer = solution([7, 2, 8, 7, 2, 5, 9], 3)
    answer = solution([1], 2)
    print(answer)


if __name__ == '__main__':
    main()
