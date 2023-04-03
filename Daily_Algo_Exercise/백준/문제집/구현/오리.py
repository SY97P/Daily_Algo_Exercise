# 2
# -1
# 1
# 10
# 3
# -1

file = open("./Daily_Algo_Exercise/백준/문제집/구현/오리.txt")

input = file.readline

for _ in range(1):
	word = input().strip()
	
	count = 0
	length = len(word)
	duck = [0 for _ in range(length)]
	template = ["q", "u", "a", "c", "k"]
	result = 0
	
	while count < length:
		curr = -1
		for i in range(length):
			if duck[i] == 0 and word[i] == template[(curr+1)%5]:
				count += 1
				duck[i] = count
				curr = (curr + 1) % 5
		print(duck)
		if count % 5 != 0 or result > 10 ** 6:
			result = -1
			break
		result += 1
	
	print(result)


file.close()