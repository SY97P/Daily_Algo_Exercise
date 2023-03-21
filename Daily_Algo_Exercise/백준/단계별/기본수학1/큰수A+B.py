# 18446744073709551615

file = open("./큰수A+B.txt")

input = file.readline


a, b = input().strip().split()
a, b = list(reversed(list(a))), list(reversed(list(b)))

if len(a) < len(b):
    a += "0" * (len(b) - len(a))
else:
    b += "0" * (len(a) - len(b))

result = ""
carry = 0
for i in range(len(a)):
    value = int(a[i]) + int(b[i]) + carry
    carry = value // 10
    value %= 10
    result += str(value)
if carry != 0:
    result += str(carry)
for r in reversed(result):
    print(r, end="")
print()


file.close()