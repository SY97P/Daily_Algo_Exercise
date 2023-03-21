# 47600

file = open("참외밭.txt")

input = file.readline


def main():
    k = int(input())
    data = []
    w, w_idx = 0, 0
    h, h_idx = 0, 0
    for i in range(6):
        dir, dist = map(int, input().split())
        if dir >= 3 and w < dist:
            w = dist
            w_idx = i
        elif dir < 3 and h < dist:
            h = dist
            h_idx = i
        data.append(dist)
    small_h = abs(data[w_idx-1] - data[(w_idx+1)%6])
    small_w = abs(data[h_idx-1] - data[(h_idx+1)%6])
    print(k * (w*h - small_w*small_h))


if __name__ == '__main__':
    main()


file.close()