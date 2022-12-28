#1 14
#2 181

file = open("./SWEA/D3/새샘이의753게임.txt", "r")

input = file.readline

t = int(input())

def dfs(index, sumof, count) : 
	if count >= 3: 
		possible.add(sumof)
		return
		
	for i in range(index + 1, 7) :
		dfs(i, sumof + num_list[i], count + 1)

for tc in range(1, t + 1) : 
	num_list = list(map(int, input().split()))

	possible = set()

	for i in range(7) : 
		dfs(i, num_list[i], 1)

	possible = list(possible)
	possible.sort(reverse = True)

	print("#%d %d" %(tc, possible[4]))

file.close()