# 402
# 1203

file = open("./ACM호텔.txt")

input = file.readline


t = int(input())
for tc in range(t):
    h, w, n = map(int, input().split())
    result = ""
    if n % h == 0:
        result = str(h)
        if n // h < 10:
            result += "0" + str(n//h)
        else:
            result += str(n//h)
    else:
        result = str(n % h)
        if n // h + 1 < 10:
            result += "0" + str(n//h+1)
        else:
            result += str(n//h+1)
    print(result)


file.close()