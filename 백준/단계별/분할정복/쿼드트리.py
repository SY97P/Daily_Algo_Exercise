# ((110(0101))(0010)1(0001))

import os
filename = "쿼드트리.txt"
file = open(os.getcwd()+"\\"+filename)

input = file.readline


def check_color(i_length, i_start, j_length, j_start):
    color = matrix[i_start][j_start]
    for i in range(i_length):
        for j in range(j_length):
            if matrix[i+i_start][j+j_start] != color:
                return -1
    return color


def quad_tree(i_length, i_start, j_length, j_start):
    if i_length <= 1 or j_length <= 1:
        print(matrix[i_start][j_start], end="")
        return

    # 해당하는 범위의 화면이 하나로 이뤄져 있는지 여부 확인
    only_one = check_color(i_length, i_start, j_length, j_start)

    if only_one >= 0:
        print(only_one, end="")
    else:
        # 여기서 분할정복
        next_i_length = i_length//2
        next_j_length = j_length//2
        odd_i_length = next_i_length if i_length%2==0 else next_i_length+1
        odd_j_length = next_j_length if j_length%2==0 else next_j_length+1

        print("(", end="")
        quad_tree(next_i_length, i_start, next_j_length, j_start)
        quad_tree(next_i_length, i_start, odd_j_length, j_start+next_j_length)
        quad_tree(odd_i_length, i_start+next_i_length, next_j_length, j_start)
        quad_tree(odd_i_length, i_start+next_i_length, odd_j_length, j_start+next_j_length)
        print(")", end="")


n = int(input())
matrix = [list(map(int, input().strip())) for _ in range(n)]

# for mat in matrix:
#     print(mat)

quad_tree(n, 0, n, 0)
print()


file.close()