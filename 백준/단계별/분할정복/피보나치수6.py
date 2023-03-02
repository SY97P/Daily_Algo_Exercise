# 517691607

file = open("피보나치수6.txt", "r")

input = file.readline


def square_matrix(n):
    if n < 2:
        return matrix
    rtn_value = square_matrix(n//2)
    if n%2 != 0:
        return multiply_matrix(multiply_matrix(rtn_value, rtn_value), matrix)
    return multiply_matrix(rtn_value, rtn_value)


def multiply_matrix(mat_a, matrix_b):
    bound = 2
    if matrix_b[0] == 1:
        bound = 1
    result = [[0 for _ in range(bound)] for _ in range(2)]
    mat_b = list(zip(*matrix_b)) if bound != 1 else [1, 0]
    for i in range(2):
        for j in range(bound):
            result[i][j] = multiply(mat_a[i], mat_b[j], bound)
    return result


def multiply(sub_a, sub_b, bound):
    result = 0
    for i in range(2):
        if bound == 1:
            result += sub_a[i] * sub_b
            continue
        result += sub_a[i] * sub_b[i]
    return result % p


def main():
    global matrix, p

    p = 1000000007
    n = int(input())
    matrix = [[1, 1], [1, 0]]
    print(multiply_matrix(square_matrix(n), matrix[1])[-1][-1] % p)


if __name__ == '__main__':
    main()


file.close()