# 2
# 4
# 3
# 2

file = open("./배.txt")

input = file.readline

n = int(input())
limit = list(map(int, input().split()))
limit.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

if limit[0] < box[0]:
    print(-1)
else:
    count = 0
    for l in limit:
        for b in box:
            if l >= b:
                box.remove(b)
                break
    count += 1

file.close()