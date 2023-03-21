# 40320
# 7712

file = open("./방사형그래프.txt")

input = file.readline


# def get_coordi(path):
#     sin = 2**0.5
#     x = [-path[7]/sin, 0, path[1]/sin, path[2], path[3]/sin, 0, -path[5]/sin, -path[6], -path[7]/sin, 0]
#     y = [path[7]/sin, path[0], path[1]/sin, 0, -path[3]/sin, -path[4], -path[5]/sin, 0, path[7]/sin, path[0]]
#     return x, y


def check(path):
    global count
    path = [path[-1]] + path + [path[0]]
    concave = False
    for i in range(1, 9):
        if 2**0.5 * path[i-1] * path[i+1] > path[i] * (path[i-1] + path[i+1]):
            concave = True
            break
    if not concave:
        count += 1


def dfs(path, visited, depth):
    if depth >= 8:
        # 여기서 count 증가하는 작업
        check(path)
    for i in range(8):
        if not visited[i]:
            visited[i] = True
            dfs(path+[abil[i]], visited, depth+1)
            visited[i] = False


def main():
    global count, abil

    for _ in range(1):
        abil = list(map(int, input().split()))
        count = 0
        for i in range(8):
            visited = [False for _ in range(8)]
            visited[i] = True
            dfs([abil[i]], visited, 1)

        print(count)


if __name__ == '__main__':
    main()


file.close()