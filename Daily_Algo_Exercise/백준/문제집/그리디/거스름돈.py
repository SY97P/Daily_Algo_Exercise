# 5
# 4

file = open('./거스름돈.txt')

input = file.readline

for _ in range(1):
    n = int(input())
    count = 0
    while True:
        # print(n, count)
        if n >= 10 and (n-10) % 2 == 0:
            n -= 10
            count += 2
            continue
        if n >= 5 and (n-5) % 2 == 0:
            n -= 5
            count += 1
            continue
        if n < 2 or n % 2 != 0:
            break
        count += n // 2
        n = 0
    print(count if n == 0 else -1)

file.close()