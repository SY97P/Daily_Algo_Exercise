# 4

file = open("./곱셈.txt", "r")

input = file.readline


def multiple(a, b, c):
    if b <= 1:
        return a % c

    if b % 2 == 0:
        return multiple(a, b//2, c)**2 % c
    else:
        return multiple(a, (b-1)//2, c)**2 * a % c


a, b, c = map(int, input().split())

print(multiple(a, b, c) % c)

file.close()
