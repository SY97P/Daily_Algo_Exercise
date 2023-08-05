# 5
# 28
# 0

file = open("C:/Users/onetu/PycharmProjects/Daily_Exercise_with_Programmers/백준/단계별/그래프순회/나이트의이동.txt", "r")

input = file.readline

from collections import deque

t = int(input())

def solve(start, end) :
    dir = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    dp[start[0]][start[1]] = 0

    q = deque([(start[0], start[1], 0)])

    while q :
        i, j, count = q.popleft()

        for dx, dy in dir :
            di = i + dx
            dj = j + dy
            if 0 <= di < n and 0 <= dj < n and count+1 < dp[di][dj] :
                dp[di][dj] = count + 1
                q.append((di, dj, dp[di][dj]))

    # for d in dp :
    #     print(d)
    return dp[end[0]][end[1]]


for tc in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    print(solve(start, end))

file.close()
