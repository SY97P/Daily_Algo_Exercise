def solution(file) : 
	for _ in range(4) : 
		obj = file.readline().strip("\n")
		tok = file.readline().strip("\n")
		answer = int(file.readline())
		file.readline()
		print(obj, tok, answer)

		index, count = 0, 0
		while index > -1 : 
			index = obj.find(tok, index)
			if index > -1 : 
				# print(index)
				index += len(tok)
				count += 1

		print(count)

# 백준 제출용
obj = input().strip("\n")
tok = input().strip("\n")

index, count = 0, 0
while index > -1 : 
	index = obj.find(tok, index)
	if index > -1 : 
		index += len(tok)
		count += 1
print(count)

def main() : 
	file = open("./그리디/문서검색tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
