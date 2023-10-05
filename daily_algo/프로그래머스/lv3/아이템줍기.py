import heapq

bound = 101


def fill_matrix(rects):
    matrix = [[0] * bound for _ in range(bound)]
    for x1, y1, x2, y2 in rects:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                matrix[x][y] = 1
    return matrix


def is_boundary(matrix, x, y):
    cnt = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x+i < bound and 0 <= y+j < bound and matrix[x+i][y+j] > 0:
                cnt += 1
    return cnt < 9


def find_boundary(matrix):
    for i in range(bound):
        for j in range(bound):
            if matrix[i][j]:
                if not is_boundary(matrix, i, j):
                    matrix[i][j] = 2
    return matrix


def get_distance(matrix, start, target):
    q = [(0, start)]
    dp = [[1e9] * bound for _ in range(bound)]
    dp[start[0]][start[1]] = 0

    while q:
        cnt, point = heapq.heappop(q)
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            di, dj = point[0] + dx, point[1] + dy
            if 0 > di or di >= bound or dj < 0 or dj >= bound:
                continue
            if matrix[di][dj] == 1 and dp[di][dj] > cnt + 1:
                dp[di][dj] = cnt + 1
                heapq.heappush(q, (dp[di][dj], (di, dj)))
    #
    # for d in dp:
    #     print(list(map(lambda x: ('00' if x == 1e9 else str(x).zfill(2)), d)))

    return dp[target[0]][target[1]]


def solution(rects, cx, cy, ix, iy):
    matrix = fill_matrix(rects)
    matrix = find_boundary(matrix)
    return get_distance(matrix, (cx*2, cy*2), (ix*2, iy*2))//2


def main():
    tc1 = [[[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8]
    answer = solution(tc1[0], tc1[1], tc1[2], tc1[3], tc1[4])
    print(answer)


main()
