def solution(file) : 
	for _ in range(3) : 
		p1, p2 = map(int, file.readline().split())
		a1, a2 = map(int, file.readline().split())
		file.readline()

		print(p1, p2)

		min_p1, min_p2 = str(p1).replace("6", "5"), str(p2).replace("6", "5")
		max_p1, max_p2 = str(p1).replace("5", "6"), str(p2).replace("5", "6")
		print(min_p1, min_p2, max_p1, max_p2)

		print(a1, a2)
		print(int(min_p1) + int(min_p2), int(max_p1) + int(max_p2))

# 백준 제출용
# p1, p2 = map(int, input().split())
# print(int(str(p1).replace("6", "5")) + int(str(p2).replace("6", "5")), int(str(p1).replace("5", "6") + int(str(p2).replace("5", "6")))
		

		

def main() : 
	file = open("./그리디/5와6의차이tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
