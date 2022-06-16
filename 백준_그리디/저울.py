from itertools import combinations
def solution(file) : 
	for _ in range(1) : 
		n = int(file.readline())
		arr = list(map(int, file.readline().split()))
		answer = int(file.readline())

		arr.sort()
		
		print(n, arr, answer)

		index = 1

		combi = set([])
		for i in range(1, len(arr)) :
			lst = list(map(sum, combinations(arr, i)))
			for l in lst :
				combi.add(l)
		print(combi)

		while True :
			if index not in combi :
				print(index)
				break
			index += 1

# 백준 제출용
n = int(input())
arr = list(map(int, input().split()))
index = 1
combi = set([])

for i in range(1, len(arr)) :
	for l in list(map(sum, combinations(arr, i))) :
		combi.add(l)

while True :
	if index not in combi :
		print(index)
		break
	index += 1
	
		

def main() : 
	file = open("./백준_그리디/저울tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
