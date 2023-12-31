# 6
# 10

file = open("./부녀회장이될테야.txt")

input = file.readline

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    building = [[1 for _ in range(n)] for _ in range(k+1)]
    building[0] = [i+1 for i in range(n)]

    for i in range(1, k+1):
        for j in range(1, n):
            building[i][j] = building[i][j-1] + building[i-1][j]

    # for b in building:
    #     print(b)
    # print()
    print(building[-1][-1])


file.close()