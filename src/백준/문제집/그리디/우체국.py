# 2

file = open("./Daily_Algo_Exercise/백준/문제집/그리디/우체국.txt")

input = file.readline 

n = int(input())

data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort()

tot_sum = 0
for l, c in data:
	tot_sum += c
# print(tot_sum)

curr = 0
for i in range(n):
	curr += data[i][1]
	if curr >= (tot_sum + 1)//2:
		print(data[i][0])
		break

file.close()