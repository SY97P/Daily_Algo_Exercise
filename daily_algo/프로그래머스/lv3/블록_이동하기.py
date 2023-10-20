from heapq import heappush, heappop


def get_next_point(point, matrix, n):
    p1, p2 = point
    next_point = set()
    if 0 < p1[0] - 1 and 0 < p2[0] - 1 and matrix[p1[0] - 1][p1[1]] == 0 and matrix[p2[0] - 1][p2[1]] == 0:
        new_point = ((p1[0] - 1, p1[1]), (p2[0] - 1, p2[1]))
        next_point.add(tuple(sorted(new_point)))
    if p1[0] + 1 <= n and p2[0] + 1 <= n and matrix[p1[0] + 1][p1[1]] == 0 and matrix[p2[0] + 1][p2[1]] == 0:
        new_point = ((p1[0] + 1, p1[1]), (p2[0] + 1, p2[1]))
        next_point.add(tuple(sorted(new_point)))
    if 0 < p1[1] - 1 and 0 < p2[1] - 1 and matrix[p1[0]][p1[1] - 1] == 0 and matrix[p2[0]][p2[1] - 1] == 0:
        new_point = ((p1[0], p1[1] - 1), (p2[0], p2[1] - 1))
        next_point.add(tuple(sorted(new_point)))
    if p1[1] + 1 <= n and p2[1] + 1 <= n and matrix[p1[0]][p1[1] + 1] == 0 and matrix[p2[0]][p2[1] + 1] == 0:
        new_point = ((p1[0], p1[1] + 1), (p2[0], p2[1] + 1))
        next_point.add(tuple(sorted(new_point)))
    if p1[0] == p2[0]:
        if 0 < p1[0] - 1 and 0 < p2[0] - 1 and matrix[p1[0] - 1][p1[1]] == 0 and matrix[p2[0] - 1][p2[1]] == 0:
            new_point = ((p1), (p1[0] - 1, p1[1]))
            next_point.add(tuple(sorted(new_point)))
            new_point = ((p2), (p2[0] - 1, p2[1]))
            next_point.add(tuple(sorted(new_point)))
        if p1[0] + 1 <= n and p2[0] + 1 <= n and matrix[p1[0] + 1][p1[1]] == 0 and matrix[p2[0] + 1][p2[1]] == 0:
            new_point = ((p1), (p1[0] + 1, p1[1]))
            next_point.add(tuple(sorted(new_point)))
            new_point = ((p2), (p2[0] + 1, p2[1]))
            next_point.add(tuple(sorted(new_point)))
    else:
        if 0 < p1[1] - 1 and 0 < p2[1] - 1 and matrix[p1[0]][p1[1] - 1] == 0 and matrix[p2[0]][p2[1] - 1] == 0:
            new_point = ((p1), (p1[0], p1[1] - 1))
            next_point.add(tuple(sorted(new_point)))
            new_point = ((p2), (p2[0], p2[1] - 1))
            next_point.add(tuple(sorted(new_point)))
        if p1[1] + 1 <= n and p2[1] + 1 <= n and matrix[p1[0]][p1[1] + 1] == 0 and matrix[p2[0]][p2[1] + 1] == 0:
            new_point = ((p1), (p1[0], p1[1] + 1))
            next_point.add(tuple(sorted(new_point)))
            new_point = ((p2), (p2[0], p2[1] + 1))
            next_point.add(tuple(sorted(new_point)))
    return next_point


def solution(board):
    n = len(board)

    matrix = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            matrix[i + 1][j + 1] = board[i][j]

    start_point = {(1, 1), (1, 2)}
    visited = [start_point]
    q = [(0, start_point)]

    while q:
        time, point = heappop(q)
        if (n, n) in point:
            return time
        next_point = get_next_point(point, matrix, n)
        for npoint in next_point:
            if npoint not in visited:
                visited.append(npoint)
                heappush(q, (time+1, npoint))

    return 0


def main():
    answer = solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
    print(answer)


if __name__ == '__main__':
    main()
