# 10
# 12
# 11

file = open("./종이의개수.txt", "r")

input = file.readline


def check_one(length, i_start, j_start):
    color = matrix[i_start][j_start]
    for i in range(length):
        for j in range(length):
            if color != matrix[i_start+i][j_start+j]:
                return 2
    return color


def enneea_tree(length, i_start, j_start):
    if length <= 1:
        count[matrix[i_start][j_start]] += 1
        return
    
    color = check_one(length, i_start, j_start)
    if color != 2:
        count[color] += 1
    else:
        # 9개로 나눔
        next_length = length // 3
        for i in range(3):
            for j in range(3):
                enneea_tree(next_length, i_start+next_length*i, j_start+next_length*j)


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# (0갯수, 1갯수, -1갯수)
count = [0, 0, 0]

# enneea- : 숫자 9 접두사
enneea_tree(n, 0, 0)

print(count[-1])
print(count[0])
print(count[1])


file.close()