def solution(file) : 
	for _ in range(3) : 
		n, l = map(int, file.readline().split())
		arr = list(map(int, file.readline().split()))
		answer = int(file.readline())
		file.readline()

		print(n, l, answer)
		print(arr)

		arr.sort()
		
		count = 0
		length = arr[0] - 0.5 + l

		while arr :
			curr = arr.pop(0)
			# 현재 지점이 테이프 길이 안에 겹치면
			# count가 0일 때는 증가
			# 아닐 때는 증가 x
			# length 변화도 안하고
			if curr + 0.5 <= length :
				if count == 0 :
					count += 1
			else :
				# 현재 지점이 테이프 길이 밖에 있으면
				# count를 증가해주고
				# length도 현재 기준으로 수정해주고
				count += 1
				length = curr - 0.5 + l
			# print("curr, length, count : ", curr, length, count)

		print(count)
		print()


# 백준 제출용
n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

count, length = 0, arr[0] - 0.5 + l

while arr :
	curr = arr.pop(0)
	if curr + 0.5 <= length :
		if count == 0 :
			count += 1
	else :
		count += 1
		length = curr - 0.5 + l
print(count)

def main() : 
	file = open("./백준_그리디/수리공항승tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
