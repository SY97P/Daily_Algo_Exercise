# 2
# 2
# 2
# 3
# 3
#
# 3
#
# 2
# 3
#
# 2
#
# 97
# 103

file = open("./소인수분해.txt")

input = file.readline


n = int(input())

if n != 1:
    prime = [False, False] + [True for _ in range(2, n+1)]

    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i+i, n+1, i):
                prime[j] = False

    if prime[n]:
        print(n)
    else:
        plist = []
        for i in range(2, n+1):
            if n % i == 0 and prime[i]:
                plist.append(i)
        temp = 1 * n
        while not prime[temp]:
            for p in plist:
                if temp % p == 0:
                    # print("info : ", temp, p)
                    temp //= p
                    print(p)
                    break
        print(temp)

file.close()