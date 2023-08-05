# 7

file = open("./백준/dp/lv1/가장긴바이토닉부분수열.txt", "r")

input = file.readline

n = int(input())

num = list(map(int, input().split()))
a = [0] + num
b = [0] + list(reversed(num))

d_inc = [0, 1] + [0 for _ in range(n - 1)]
d_dec = [0, 1] + [0 for _ in range(n - 1)]

# 증가하는 부분수열 길이 구하기
for i in range(2, n + 1) : 
	for j in range(i-1, -1, -1) : 
		if a[i] > a[j] : 
			d_inc[i] = max(d_inc[i], d_inc[j] + 1)
		if b[i] > b[j] : 
			d_dec[i] = max(d_dec[i], d_dec[j] + 1)

d_inc = d_inc[1:]
d_dec = list(reversed(d_dec[1:]))

length = 0
for i in range(n) :
	length = max(length, d_inc[i] + d_dec[i] - 1)

print(length)

file.close()