# 10

file = open("./이항계수3.txt", "r")

input = file.readline


p = 10**9+7


# n! mod p
def factorial(n):
    result = 1
    while n > 1:
        result = (result * n) % p
        n -= 1
    return result


# a^(t-2) mod t -> (k!(n-k)!)^(p-2) mod p
def pow(a, tt):
    if tt <= 1:
        return a % p
    result = pow(a, tt//2)**2 % p
    if tt%2 != 0:
        result *= a % p
    return result


n, k = map(int, input().split())

numerator = factorial(n)
denominator = pow(factorial(k) * factorial(n-k), p-2)

print(numerator * denominator % p)


file.close()