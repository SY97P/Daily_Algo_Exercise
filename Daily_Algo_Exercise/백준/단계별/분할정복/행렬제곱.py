# 0 0
# 0 0
#
# 69 558
# 337 406
#
# 468 576 684
# 62 305 548
# 656 34 412
#
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512

file = open("./행렬제곱.txt", "r")

input = file.readline


def square_matrix(b):
    if b <= 1:
        return matrix
    rtn_matrix = square_matrix(b//2)
    if b%2 == 0:
        return matrix_multiply(rtn_matrix, rtn_matrix)
    return matrix_multiply(matrix_multiply(rtn_matrix, rtn_matrix), matrix)


def matrix_multiply(mat_a, matrix_b):
    mat_b = list(zip(*matrix_b))
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = multiply(mat_a[i], mat_b[j])
    return result


def multiply(sub_a, sub_b):
    result = 0
    for i in range(n):
        result += sub_a[i] * sub_b[i]
    return result % MODULER


def print_matrix(matrix):
    for mat in matrix:
        print(*mat)


def main():
    global n, matrix, square, MODULER

    MODULER = 1000

    n, b = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] %= MODULER

    print_matrix(square_matrix(b))


if __name__ == '__main__':
    main()

file.close()
