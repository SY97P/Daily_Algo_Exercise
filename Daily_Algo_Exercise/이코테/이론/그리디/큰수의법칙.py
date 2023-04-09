n, m, k = map(int, input().split())

alist = list(map(int, input().split()))

alist.sort()

a, b = alist[-1], alist[-2]

count = m // (k + 1) * k + m % (k + 1)

result = count * a + (m - count) * b

print(result)