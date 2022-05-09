import random
def solution(n, arr) : 
	answer = 0 

	arr = sorted(arr)

	start, end = arr.pop(0)

	isFirst = False
	
	while arr : 
		n_start, n_end = arr.pop(0)

		# 첫 회의 선택
		# 지금 회의 끝이 다음 회의 끝보다 크면 다음 회의
		# 지금 회의 끝이 다음 회의 끝보다 작거나 같으면 지금 회의
		if not isFirst : 
			if end >= n_end :
				start, end = n_start, n_end
			answer += 1
			isFirst = True
		# 첫 회의가 잡혔으면 다음 회의 시작이 지금 회의 끝보다 크거나 같아야 함. 
		else : 
			# 가능한 다음 회의면 회의 잡음
			if end <= n_start :
				answer += 1
				start, end = n_start, n_end
			# 다음 회의가 지금 회의보다 빨리 끝나면 지금 회의 취소하고 다음 회의
			# 다음 회의가 지금 회의보다 늦게 끝나면 그대로 지나감. 
			else : 
				if n_end < end : 
					start, end = n_start, n_end
			
			
	return answer

n = int(input())
arr = sorted([tuple(map(int, input().split())) for i in range(n)])
start, end = arr.pop(0)
isFirst = False
answer = 0
while arr : 
	n_start, n_end = arr.pop(0)

	if not isFirst : 
		if end >= n_end : 
			start, end = n_start, n_end
			answer += 1
			isFirst = True
	else : 
		if end <= n_start : 
			answer += 1
			start, end = n_start, n_end
		else : 
			if n_end < end : 
				start, end = n_start, n_end
print(answer)
		

def main() : 
	# file = open("./백준_그리디/회의실배정.txt", 'r')
	# n = int(file.readline())
	# arr = []
	# for i in range(n) : 
	# 	arr.append(tuple(map(int, file.readline().split())))

	for i in range(10) : 
		print(random.randrange(1,15))

	# n = 10
	# arr = [(random.randrange(1, 15), random.randrange(1,15)) for i in range(n)]
	# for i, a in enumerate(arr) : 
	# 	arr[i] = sorted(arr[i])
	# print(arr)

	# print("solution : ", solution(n, arr))
	
	# file.close()

main()
