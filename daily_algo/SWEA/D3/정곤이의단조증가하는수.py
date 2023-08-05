file = open("./Daily_Algo_Exercise/SWEA/D3/정곤이의단조증가하는수.txt")

input = file.readline

def check(arr):
	arr = str(arr)
	for i in range(len(arr)-1):
		if arr[i] > arr[i+1]:
			return False
	return True

t = int(input())
for tc in range(1, t+1):
	answer = -1
	n = int(input())
	arr = list(map(int, input().split()))

	for i in range(n):
		for j in range(i+1, n):
			val = arr[i] * arr[j]
			if answer < val and check(val):
				answer = val

	print(f'#{tc} {answer}')
	

file.close()