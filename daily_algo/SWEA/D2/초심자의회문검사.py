#1 1
#2 0
#3 1
#4 0
#5 1
#6 0
#7 1
#8 0
#9 0
#10 1

file = open("./SWEA/D2/초심자의회문검사.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) :
	word = input().strip()

	length = len(word)

	isPalindrome = True
	
	for i in range(length // 2) : 
		if word[i] != word[length - 1 - i] : 
			isPalindrome = False
			break

	if isPalindrome : 
		print("#%d %d" %(tc, 1))
	else: 
		print("#%d %d" %(tc, 0))
		

file.close()