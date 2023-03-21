# 33
# 14
# -1

file = open("./백준/dp/연속합.txt", "r")

input = file.readline

def solve() : 
	for i in range(1, n + 1) : 
		d.append(max(num[i] + d[i-1], num[i]))

# for _ in range(3) : 
n = int(input())
num = [0] + list(map(int, input().split()))

d = [0]

solve()

# print(num)
# print(d)

print(max(d[1:]))

file.close()