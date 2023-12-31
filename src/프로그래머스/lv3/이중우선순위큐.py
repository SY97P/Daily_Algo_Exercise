from heapq import heappush, heappop


def solution(operations):
    max_heap, min_heap = [], []

    for operation in operations:
        op, nu = operation.split()
        nu = int(nu)

        if op == 'I':
            heappush(max_heap, -nu)
            heappush(min_heap, nu)
        else:
            if not min_heap or not max_heap:
                continue
            if nu == 1:
                item = heappop(max_heap)
                min_heap.remove(-item)
            else:
                item = heappop(min_heap)
                max_heap.remove(-item)

    if not min_heap or not max_heap:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]


def main():
    answer = solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
    answer = solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
    print(answer)


if __name__ == '__main__':
    main()