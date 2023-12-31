# 1 (a)
# 4 (aaba)
# 5 (abcbc)
# 3 (aba)
# 2 (ab)
# 3 (bca)
# 2 (bc)
# 5 (abaab)

file = open("./광고.txt", "r")

input = file.readline


def failure_function():
    pi = [0 for _ in range(n)]
    j = 0
    for i in range(1, n):
        while j>0 and t[i] != t[j]:
            j = pi[j-1]
        if t[i] == t[j]:
            j += 1
            pi[i] = j
    return pi


n = int(input())
t = input().replace('\n', '')

pi = failure_function()

print(n - pi[n-1])


file.close()