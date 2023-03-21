# 9
# 7

file = open(
    file="./색종이만들기.txt",
    mode="r"
)

input = file.readline


debug = False
num = chr(ord('a'))


def fill_color(i_length, i_start, j_length, j_start):
    global num
    for i in range(i_start, i_start+i_length):
        for j in range(j_start, j_start+j_length):
            matrix[i][j] = num
    num = chr(ord(num)+1)


def count(color):
    global white, blue
    if color == 0:
        white += 1
    else :
        blue += 1


def divide_and_conquer(i_length, i_start, j_length, j_start):
    global num

    color = matrix[i_start][j_start]

    if debug:
        print(i_start, i_length, j_start, j_length)

    if i_length <= 1 and j_length <= 1:
        count(color)
        if debug:
            fill_color(i_length, i_start, j_length, j_start)
        return

    # 해당 구간이 하나의 색으로만 이뤄져 있는지 확인
    only_one = True
    for i in range(i_start, i_start+i_length):
        for j in range(j_start, j_start+j_length):
            if color != matrix[i][j]:
                only_one = False
                break

    if debug:
        print("only_one : ", only_one)

        for i in range(i_start, i_start+i_length):
            for j in range(j_start, j_start+j_length):
                print(matrix[i][j], end=" ")
            print()
        print()

    if only_one:
        count(color)
        # fill_color(i_length, i_start, j_length, j_start)
    else:
        next_i_length = i_length // 2
        next_j_length = j_length // 2
        odd_i_length = next_i_length
        odd_j_length = next_j_length
        if next_i_length != 1 and next_i_length % 2 != 0:
            odd_i_length += 1
        if next_j_length != 1 and next_j_length % 2 != 0:
            odd_j_length += 1
        divide_and_conquer(next_i_length, i_start, next_j_length, j_start)
        divide_and_conquer(next_i_length, i_start, odd_j_length, j_start+next_j_length)
        divide_and_conquer(odd_i_length, i_start+next_i_length, next_j_length, j_start)
        divide_and_conquer(odd_i_length, i_start+next_i_length, odd_j_length, j_start+next_j_length)


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

if debug:
    for mat in matrix:
        print(mat)

white = blue = 0

divide_and_conquer(n, 0, n, 0)

print(white)
print(blue)

if debug:
    for mat in matrix:
        print(mat)


file.close()