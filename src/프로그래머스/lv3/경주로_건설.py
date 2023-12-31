from heapq import heappush, heappop


def solution(board):
    n = len(board)
    # 0:e 1:s 2:w 3:n
    dlist = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dp = [[[1e9]*4 for _ in range(n)] for _ in range(n)]
    for dir in range(4):
        dp[0][0][dir] = 0

    q = [(dp[0][0][0], 0, 0, 0), (dp[0][0][1], 0, 0, 1)]

    while q:
        cost, x, y, dir = heappop(q)
        if dp[x][y][dir] < cost:
            continue
        for ndir, (dx, dy) in enumerate(dlist):
            di, dj = x + dx, y + dy
            if 0 <= di < n and 0 <= dj < n and board[di][dj] == 0:
                ncost = cost + 100
                if (dir + 1) % 2 == ndir % 2:
                    ncost += 500
                if dp[di][dj][ndir] > ncost:
                    dp[di][dj][ndir] = ncost
                    heappush(q, (dp[di][dj][ndir], di, dj, ndir))

    return min(dp[n - 1][n - 1])


def main():
    answer = solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    print(answer)


if __name__ == '__main__':
    main()
