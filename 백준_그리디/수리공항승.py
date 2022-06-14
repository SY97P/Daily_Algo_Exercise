def solution(file) : 
	for _ in range(3) : 
		n, l = map(int, file.readline().split())
		arr = list(map(int, file.readline().split()))
		answer = int(file.readline())
		file.readline()

		print(n, l, answer)
		print(arr)

		count = 0 

		arr.sort()

		while arr : 
			curr = arr.pop(0)
			length = curr - 0.5 + l
			count += 1
			print(curr, length)
			if len(arr) != 0 and l >= arr[0] + 0.5 : 
				arr.pop(0)

		print(count)

def main() : 
	file = open("./백준_그리디/수리공항승tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
