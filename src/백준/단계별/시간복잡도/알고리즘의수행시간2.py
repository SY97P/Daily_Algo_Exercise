# 7
# 1

file = open("./알고리즘의수행시간2.txt")

input = file.readline


def MenOfPassion(alist, n):
    global count

    sum = 0
    for i in range(1, n+1):
        count += 1
        sum += alist[i]
    return sum


n = int(input())
count = 0
MenOfPassion([i for i in range(n+1)], n)

print(count)
print(count // n)


file.close()