# 4
# 2
# 999999901

file = open("./달팽이는올라가고싶다.txt")

input = file.readline


import math


def main():
    for _ in range(5):
        a, b, v = map(int, input().split())
        value = 1 + math.ceil((v-a)/(a-b))
        print(value)


if __name__ == '__main__':
    main()


file.close()