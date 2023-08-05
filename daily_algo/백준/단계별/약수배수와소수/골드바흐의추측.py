# 3 5
# 5 5
# 5 11

file = open("./골드바흐의추측.txt")

input = file.readline


t = int(input())
for _ in range(t):
    n = int(input())

    prime = [False, False] + [True for _ in range(2, n+1)]

    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i+i, n+1, i):
                prime[j] = False

    plist = [i for i in range(n+1) if prime[i]]

    # print(n)
    # print(plist)

    result_i = result_j = 0
    i, j = 0, len(plist)-1
    while i <= j:
        sumof = plist[i] + plist[j]
        # print(i, j, plist[i], plist[j], sumof)
        if sumof == n:
            result_i, result_j = i, j
            i += 1
            j -= 1
        elif sumof < n:
            i += 1
        else:
            j -= 1
    print(plist[result_i], plist[result_j])


file.close()