# 8
# 4000

file = open("./히스토그램에서가장큰직사각형.txt", "r")

input = file.readline

#
# def solve(low, high):
#     mid = (low+high)//2
#
#     left = solve(low, mid-1)
#     right = solve(mid+1, high)
#     val = get_count(mid)
#
#     return max(left)


def main():
    global hist
    while True:
        line = input().strip()
        if line == "0":
            break
        hist = list(map(int, line.split()))

        solve(0, len(hist)-1)


if __name__ == '__main__':
    main()


file.close()