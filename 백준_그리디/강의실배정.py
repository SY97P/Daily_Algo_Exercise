def solution(file) :
	for _ in range(1) :
		n = int(file.readline())
		arr = []
		for _ in range(n) :
			arr.append(list(map(int, file.readline().split())))
		answer = int(file.readline())

		arr.sort()
		
		print(n, arr, answer)

def main() :
	file = open("./백준_그리디/강의실배정tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
