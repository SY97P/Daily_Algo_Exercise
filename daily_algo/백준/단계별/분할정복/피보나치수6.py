# 517691607

file = open("피보나치수6.txt", "r")

input = file.readline


def square_matrix(n):
    if n < 2:
        return matrix
    rtn_value = square_matrix(n//2)
    if n % 2 == 0:
        return multiply_matrix(rtn_value, rtn_value)
    return multiply_matrix(multiply_matrix(rtn_value, rtn_value), matrix)


def multiply_matrix(mat_a, mat_b):
    result = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            result[i][j] = multiply(mat_a[i], mat_b[j])
    return result


def multiply(sub_a, sub_b):
    result = 0
    for i in range(2):
        result += sub_a[i] * sub_b[i]
    return result % p


def main():
    global matrix, p
    p = 1000000007
    n = int(input())
    matrix = [[1,1], [1,0]]
    print(square_matrix(n)[1][0] % p)


if __name__ == '__main__':
    main()


file.close()