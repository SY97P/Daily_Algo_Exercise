def solution(tc) : 
	for item in tc : 
		arr, answer = item
		print(arr, answer)

		arr.sort()
		print(arr)

		result = 0
		# 홀수이면 True
		if len(arr) % 2 != 0 :
			result += arr.pop(0)

		while arr : 
			result += arr.pop(0) * arr.pop(0)

		print(result)

def main() : 
	tc = [
		[[4,-1,2,1,3],6],
		[[6,0,1,2,4,3,5],27],
		[[1,-1],-1],
		[[3,-1,0,1],1],
		[[2,1,1],2]
	]

	print("solution : ", solution(tc))

main()