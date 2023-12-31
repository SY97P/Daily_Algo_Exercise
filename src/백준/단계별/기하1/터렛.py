# 2
# 1
# 0

file = open("./터렛.txt")

input = file.readline


def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def main():
    t = int(input())
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        distance = dist(x1, y1, x2, y2)
        range_dist = r1 + r2
        min_r = min(r1, r2)
        max_r = max(r1, r2)
        sum_r = r1 + r2

        if x1 == x2 and y1 == y2:
            if r1 == r2:
                if r1 == 0:
                    print(0)
                else:
                    print(-1)
            else:
                print(0)
        elif distance == max_r:
            if min_r == 0:
                print(1)
            else:
                print(2)
        elif distance < max_r:
            if distance + min_r > max_r:
                print(2)
            elif distance + min_r == max_r:
                print(1)
            else:
                print(0)
        elif distance > max_r:
            if distance < sum_r:
                print(2)
            elif distance == sum_r:
                print(1)
            else:
                print(0)
        else:
            print("Exception Occured")



if __name__ == '__main__':
    main()


file.close()