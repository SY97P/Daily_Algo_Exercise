def oddCount(dic) : 
	count = 0
	for value in dic.values() :
		if value % 2 != 0 :
			count += 1
		if count > 1 : 
			return True
	return False
	
def solution(file) :
	for _ in range(8) :
		token = file.readline().strip("\n")
		answer = file.readline().strip("\n")
		file.readline()

		print(token, answer)

		dic = dict()

		for t in token :
			if t in dic.keys() :
				dic[t] += 1
			else :
				dic[t] = 1
		print(dic)

		lst = list(map(list, dic.items()))
		lst.sort()
		print(lst)

		if oddCount(dic) :
			print("I'm Sorry Hansoo")
		else :
			result = ""
			for l in lst : 
				result += l[0] * (l[1] // 2)
				l[1] -= (l[1] // 2) * 2
				print(result, l[1])
			print(lst)
			index = len(result)
			result += max(lst, key = lambda x: x[1])[0] if max(lst, key = lambda x: x[1])[1] != 0 else ""
			for i in range(index-1, -1, -1) :
				result += result[i]
			print(result)
		print()

# 백준 제출용
def oddCount(dic) : 
	count = 0
	for value in dic.values() :
		if value % 2 != 0 :
			count += 1
		if count > 1 : 
			return True
	return False
	
token = input().strip("\n")
dic = dict()
for t in token :
	if t in dic.keys() :
		dic[t] += 1
	else : 
		dic[t] = 1
lst = list(map(list, dic.items()))
lst.sort()

if oddCount(dic) :
	print("I'm Sorry Hansoo")
else  :
	result = ""
	for l in lst :
		result += l[0] * (l[1] // 2)
		l[1] -= (l[1] // 2) * 2
	index = len(result)
	result += max(lst, key = lambda x: x[1])[0] if max(lst, key = lambda x: x[1])[1] != 0 else ""
	for i in range(index-1, -1, -1) :
		result += result[i]
	print(result)
				
		

def main() :
	file = open("./그리디/팰린드롬만들기tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
