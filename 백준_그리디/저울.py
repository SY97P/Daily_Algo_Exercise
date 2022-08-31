file = open("./백준_그리디/저울tc.txt", "r")


for tc in range(1) :
	n = int(file.readline())
	weights = list(map(int, file.readline().split()))
	answer = int(file.readline())
	file.readline()

	weights.sort()

	print(n, answer)
	print(weights)

	dp = set()

	for weight in weights :
		if not dp : 
			dp.add(weight)
			continue
		temp = set()
		for dp_item in dp :
			print("dp_item : ", dp_item)
			temp.add(dp_item + weight)
		dp.update(temp)
		print(weight, dp)

	print(dp)

	index = 1
	for dp_item in list(dp) : 
		if dp_item != index :
			print(index)
			break
		index += 1


file.close()

# 백준 제출용

