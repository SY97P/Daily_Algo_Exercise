# 20 Sunyoung
# 21 Junkyu
# 21 Dohyun

file = open("./나이순정렬.txt")

input = file.readline

n = int(input())
data = [list(input().split()) for _ in range(n)]
data.sort(key=lambda x: int(x[0]))

for d in data:
    print(*d)

file.close()