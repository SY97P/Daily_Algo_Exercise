from collections import defaultdict
from heapq import heappush, heappop
from itertools import permutations

answer = 1e9
bound = 4
dlist = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_card_cnt(board):
    return max([max(b) for b in board])


def get_card_loc(board):
    card_loc = defaultdict(list)
    for i in range(bound):
        for j in range(bound):
            if board[i][j] != 0:
                card_loc[board[i][j]].append((i, j))
    return card_loc


def get_dist(s, e, board):
    dp = [[1e9] * bound for _ in range(bound)]
    dp[s[0]][s[1]] = 0
    q = [(0, s)]

    while q:
        dist, point = heappop(q)
        if dp[point[0]][point[1]] < dist:
            continue
        if point == e:
            continue
        for dx, dy in dlist:
            di, dj = point[0] + dx, point[1] + dy
            if 0 <= di < bound and 0 <= dj < bound and dp[di][dj] < dist + 1:
                dp[di][dj] = dist + 1
                heappush(q, (dp[di][dj], (di, dj)))
        for dx, dy in dlist:
            di, dj = point[0], point[1]
            while 0 <= di+dx < bound and 0 <= dj+dy < bound and board[di][dj] == 0:
                di, dj = di + dx, dj + dy
            if 0 <= di < bound and 0 <= dj < bound and dp[di][dj] > dist + 1:
                dp[di][dj] = dist + 1
                heappush(q, (dp[di][dj], (di, dj)))

    return dp[e[0]][e[1]]


def solution(board, r, c):
    global answer
    card_cnt = get_card_cnt(board)
    card_loc = get_card_loc(board)

    def solve(point, idx, cards, dist):
        global answer
        if answer < dist: return
        if idx >= card_cnt:
            answer = min(answer, dist)
            return
        card = cards[idx]

        adist = get_dist(point, card_loc[card][0], board)
        board[card_loc[card][0][0]][card_loc[card][0][1]] = 0
        cdist = get_dist(card_loc[card][0], card_loc[card][1], board)
        board[card_loc[card][1][0]][card_loc[card][1][1]] = 0
        solve(card_loc[card][1], idx + 1, cards, dist + adist + cdist + 2)

        bdist = get_dist(point, card_loc[card][1], board)
        board[card_loc[card][1][0]][card_loc[card][1][1]] = 0
        cdist = get_dist(card_loc[card][0], card_loc[card][1], board)
        board[card_loc[card][0][0]][card_loc[card][0][1]] = 0
        solve(card_loc[card][0], idx + 1, cards, dist + bdist + cdist + 2)

    for cards in permutations(range(1, card_cnt + 1), card_cnt):
        solve((r, c), 0, cards, 0)

    return answer


def main():
    answer = solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
    print(answer)


if __name__ == '__main__':
    main()
