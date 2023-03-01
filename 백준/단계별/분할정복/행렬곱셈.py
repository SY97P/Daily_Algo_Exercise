# -1 -2 6
# -3 -6 12
# -5 -10 18

file = open("./행렬곱셈.txt", "r")

input = file.readline


# return list(zip(*mat_b)) 이렇게 해도 됨
def optimize(mat_b, m, k):
    return [[mat_b[i][j] for i in range(m)] for j in range(k)]


def matrix_multiply(matrix_a, matrix_b, n, m, k):
    result = [[0 for _ in range(n)] for _ in range(k)]
    for i in range(n):
        for j in range(k):
            result[i][j] = multiply(matrix_a[i], matrix_b[j], m)
    print_matrix(result)


def multiply(mat_a, mat_b, m):
    result = 0
    for i in range(m):
        result += mat_a[i] * mat_b[i]
    return result


def print_matrix(matrix):
    for mat in matrix:
        print(*mat)


def main():
    n, m = map(int, input().split())
    matrix_a = [list(map(int, input().split())) for _ in range(n)]
    m, k = map(int, input().split())
    mat_b = [list(map(int, input().split())) for _ in range(m)]
    matrix_b = optimize(mat_b, m, k)

    print(list(zip(*mat_b)))

    # for mat in matrix_b:
    #     print(mat)

    matrix_multiply(matrix_a, matrix_b, n, m, k)


if __name__ == '__main__':
    main()


file.close()
