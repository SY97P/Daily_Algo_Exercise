# 0
# 1

file = open("./점근적표기1.txt")

input = file.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 == c:
    print(1 if a0 <= 0 else 0)
elif a1 > c:
    print(0)
else:
    print(1 if (c-a1)*n0 >= a0 else 0)

file.close()