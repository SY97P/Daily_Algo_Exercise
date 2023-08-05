# 1
# 0

file = open("./알고리즘의수행시간1.txt", "r")

input = file.readline


def MenOfPassion(alist,  n):
    i = n//2
    return alist[i]


n = int(input())
count = 1
MenOfPassion([i for i in range(n+1)], n)

print(count)
print(count // count - 1)


file.close()