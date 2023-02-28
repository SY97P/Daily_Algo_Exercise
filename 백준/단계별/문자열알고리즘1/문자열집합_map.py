# 4

file = open("./문자열집합.txt", "r")

input = file.readline

# 1. set 방식
# n, m = map(int, input().split())
# word_set = set()
# for _ in range(n):
#     word_set.add(input().strip())
# count = 0
# for _ in range(m):
#     if input().strip() in word_set:
#         count += 1
# print(count)

from collections import defaultdict

n, m = map(int, input().split())
dic = defaultdict(bool)
for _ in range(n):
    dic[input().strip()] = True
count = 0
for _ in range(m):
    if dic[input().strip()]:
        count += 1
print(count)

file.close()