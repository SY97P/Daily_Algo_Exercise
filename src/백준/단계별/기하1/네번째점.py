# 7 7
# 30 10

file = open("./네번째점.txt")

input = file.readline

from collections import defaultdict

x = defaultdict(int)
y = defaultdict(int)

for _ in range(3):
    a, b = map(int, input().split())
    x[a] += 1
    y[b] += 1

for key, value in x.items():
    if value % 2 != 0:
        print(key, end=" ")
        break
for key, value in y.items():
    if value % 2 != 0:
        print(key)
        break


file.close()