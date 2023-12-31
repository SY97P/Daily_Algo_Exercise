#1 1	// Test Case 1의 정답
#2 2	// Test Case 2의 정답
#3 3	// Test Case 3의 정답

file = open("./SWEA/D4/자기방으로돌아가기.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	n = int(input())

	corr = [0 for _ in range(200)]

	for _ in range(n) : 
		start, end = map(int, input().split())

		temp = min(start, end)
		end = (max(start, end) - 1)//2
		start = (temp - 1)//2

		for i in range(start, end + 1) : 
			corr[i] += 1

		# print(corr)

	print("#%d %d" % (tc, max(corr)))

file.close()