# 3
# 0

# 2
# 5
# 3

file = open('./어린왕자.txt')

input = file.readline


# 내부면 1
# 외부면 0
def check(x1, y1, x2, y2, r):
    return 1 if ((x1-x2)**2 + (y1-y2)**2)**0.5 < r else 0


def main():
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        count = 0
        for _ in range(n):
            cx, cy, r = map(int, input().split())
            if check(x1, y1, cx, cy, r) + check(x2, y2, cx, cy, r) == 1:
                count += 1
        print(count)


if __name__ == '__main__':
    main()


file.close()