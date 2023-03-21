# 1
# 0

file = open("./선분교차1.txt")

input = file.readline

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    a = 0 if x2 - x1 == 0 else (y2-y1) / (x2-x1)
    b = y1 - a * x1

    c = 0 if x4 - x3 == 0 else (y4-y3) / (x4-x3)
    d = y3 - c * x3

    result = 0
    if a - c != 0:
        cross_x = (d-b) / (a-c)
        cross_y = a * cross_x + b
        if min(x1, x2) <= cross_x <= max(x1, x2) and min(x3, x4) <= cross_x <= max(x3, x4) and min(y1, y2) <= cross_y <= max(y1, y2) and min(y3, y4) <= cross_y <= max(y3, y4):
            result = 1
        print(result)
    else:
        if (x1 == x3 and y1 == y3) or (x1 == x4 and y1 == y4) or (x2 == x3 and y2 == y3) or (x2 == x4 and y2 == y4):
            result = 1
        print(result)

file.close()