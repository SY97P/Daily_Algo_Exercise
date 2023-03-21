# 35
# 3

file = open("./알고리즘의수행시간2.txt")

input = file.readline

#
# def MenOfPassion(A, n):
#     count = 0
#     sum = 0
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 count += 1
#                 print(count, i, j, k)
#                 sum = sum + A[i] * A[j] * A[k] # 코드1
#     print(count)
#     return sum



n = int(input())
# MenOfPassion([i for i in range(n)], n)

print(n*(n-2)*(n-3)//4)
print(3)

file.close()