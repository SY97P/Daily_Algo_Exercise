def solution(file) :
	for _ in range(3) :
		n, k = map(int, file.readline().split())
		token = list(file.readline().rstrip("\n"))
		answer = int(file.readline())
		file.readline()
   
		print(n, k, token, answer)

		count = 0
		result = ""
		key = ""
		for i in range(n) :
			if key == "" :
				key = int(token[i])
				result = 
				continue
			if count == k :
				result += str(token)[i:]
				break
			if int(token[i]) < key :
				count += 1			
			else :
				key = int(token[i])
				result += str(key)  

		print(result)
				

def main() :
	file = open("./백준_그리디/크게만들기tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
