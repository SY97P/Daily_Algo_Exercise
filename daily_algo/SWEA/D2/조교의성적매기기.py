#1 A-
#2 C-
#3 C0
#4 A-
#5 C0
#6 A-
#7 C+
#8 C+
#9 B0
#10 A0

file = open("./SWEA/D2/조교의성적매기기.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	n, k = map(int, input().split())
	scores = []
	for _ in range(n) : 
		mi, fi, ho = map(int, input().split())
		scores.append(mi * 35 + fi * 45 + ho * 20)

	grade = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
	
	target = scores[k-1]
	scores.sort(reverse = True)

	result = grade[scores.index(target) // (n // 10)]

	print("#%d %s" % (tc, result))
	

file.close()