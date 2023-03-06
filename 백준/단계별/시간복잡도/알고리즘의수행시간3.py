# 49
# 2

file = open("./알고리즘의수행시간2.txt")

input = file.readline


# 이렇게 풀어야 시간초과없이 pass 가능
# -> n <= 5000000000
# n = int(input())
# print(n**2)
# print(2)


def MenOfPassion(A, n):
    count = 0
    sum = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            count += 1
            sum += A[i] * A[j]
    return count


n = int(input())
count = MenOfPassion([i for i in range(n+1)], n)

print(count)
degree = 0
while count >= n:
    count //= n
    degree += 1
print(degree)


file.close()