# 9
# 10
# 9
# -1
# -1
# 6

import os

filename = "다리만들기2.txt"
file = open(os.getcwd() + "\\" + filename)

input = file.readline

import sys, heapq

# input = sys.stdin.readline

log = False


def prim():
    q = [(0, 1)]
    heapq.heapify(q)

    visited = [False for _ in range(island)]

    result = 0

    while q:
        cost, node = heapq.heappop(q)

        if not visited[node]:
            visited[node] = True
            result += cost

            for next_node, next_cost in enumerate(adj[node]):
                if not visited[next_node] and next_cost != float('inf'):
                    heapq.heappush(q, (next_cost, next_node))

    if False in visited[1:]:
        result = -1

    return result


def dist(i, j, start, dir, count):
    di, dj = i + dir[0], j + dir[1]
    if 0 <= di < n and 0 <= dj < m:
        end = matrix[di][dj] - 1
        if end + 1 == 0:
            dist(di, dj, start, dir, count + 1)
        elif end == start:
            return
        else:
            if count < 2:
                return
            adj[start][end] = adj[end][start] = min(adj[start][end], adj[end][start], count)
            return


def number(i, j, num):
    for dx, dy in d:
        di = i + dx
        dj = j + dy
        if 0 <= di < n and 0 <= dj < m and matrix[di][dj] == 1:
            matrix[di][dj] = island
            number(di, dj, num)


# for _ in range(6):
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

if log:
    for mat in matrix:
        print(mat)

# 섬 번호 매기기
island = 1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            island += 1
            matrix[i][j] = island
            number(i, j, island)

if log:
    print("island : ", island)
    print()
    for mat in matrix:
        print(mat)

# 섬 사이 거리 구하기
adj = [[float('inf') for _ in range(island)] for _ in range(island)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 0:
            for dir in d:
                dist(i, j, matrix[i][j] - 1, dir, 0)

if log:
    print()
    for ad in adj:
        print(ad)

# 프림 알고리즘으로 MST구하기
print(prim())

file.close()
