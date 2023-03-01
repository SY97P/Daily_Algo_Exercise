# 10

file = open("C:/Users/onetu/PycharmProjects/Daily_Exercise_with_Programmers/백준/단계별/분할정복/이항계수3.txt", "r")

input = file.readline


# * 이항계수
# - 조합론 / 페르마의 소정리 / 모듈러 곱셈 역원 / 분할정복 / DP
# - 5^3 mod 3 = 5 mod 3
# - a^t mod t = a mod t
# - a^(t-2) mod t = a^-1 mod t


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