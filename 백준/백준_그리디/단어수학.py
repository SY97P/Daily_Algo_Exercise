def solution(file) : 
	for _ in range(4) : 
		n = int(file.readline())
		words = [file.readline().strip("\n") for _ in range(n)]
		answer = int(file.readline())
		dic = dict()

		for word in words : 
			for i in range(len(word)-1, -1, -1) : 
				if word[i] in dic : 
					dic[word[i]] += pow(10, (len(word)-i-1))
				else : 
					dic[word[i]] = pow(10, (len(word)-i-1))
		print(dic)
		lst = []
		for key in dic.keys() : 
			lst.append([key, dic.get(key)])
		lst.sort(key = lambda x : x[1], reverse = True)
		print(lst)

		value = 9
		for i, l in enumerate(lst) : 
			dic[lst[i][0]] *= value
			value -= 1
		print(dic)

		result = 0
		for val in dic.values() : 
			result += val
		print(result, answer)

# 백준 제출용
n = int(input())
words = [input().strip("\n") for _ in range(n)]
dic = dict()

for word in words : 
	for i in range(len(word)-1, -1, -1) :
		if word[i] in dic : 
			dic[word[i]] += pow(10, (len(word)-i-1))
		else : 
			dic[word[i]] = pow(10, (len(word)-i-1))
lst = []
for key in dic.keys() : 
	lst.append([key, dic.get(key)])
lst.sort(key = lambda x: x[1], reverse = True)

value = 9
for i, l in enumerate(lst) : 
	dic[lst[i][0]] *= value
	value -= 1
result = 0
for val in dic.values() : 
	result += val
print(result)

def main() : 
	file = open("./백준_그리디/단어수학tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
