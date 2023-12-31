# 100.0

file = open("./다각형의면적.txt")

input = file.readline


def main():
    n = int(input())
    coordis = [tuple(map(int, input().split())) for _ in range(n)]
    coordis.append(coordis[0])

    xr = yr = 0
    for i in range(n):
        xr += coordis[i][0] * coordis[i+1][1]
        yr += coordis[i][1] * coordis[i+1][0]

    result = abs(xr - yr) / 2
    print(round(result, 1))


if __name__ == '__main__':
    main()


file.close()