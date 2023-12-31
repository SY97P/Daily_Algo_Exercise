# 2 3 0 3 1
#
# 1 0 1 0 1 0

file = open("./좌표압축.txt")

input = file.readline

n = int(input())
coordis = list(map(int, input().split()))

coordi = list(set(coordis))
coordi.sort()

# print(coordi)

dic = dict()
for i in range(len(coordi)):
    dic[coordi[i]] = i

for coor in coordis:
    print(dic[coor], end=" ")


file.close()