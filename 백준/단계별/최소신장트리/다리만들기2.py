# 9
# 10
# 9
# -1

import os
filename = "다리만들기2.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline

log = True

def number(i, j, num) :
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] :
        di = i + dx
        dj = j + dy
        if 0 <= di < n and 0 <= dj < m and matrix[di][dj] == 1 :
            matrix[di][dj] = island
            number(di, dj, num)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

if log :
    for mat in matrix :
        print(mat)

# 섬 번호 매기기
island = 1
for i in range(n) :
    for j in range(m) :
        if matrix[i][j] == 1:
            island += 1
            matrix[i][j] = island
            number(i, j, island)

if log :
    print()
    for mat in matrix :
        print(mat)

# 섬 사이 거리 구하기
adj = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n) :
    for j in range(m) :




file.close()