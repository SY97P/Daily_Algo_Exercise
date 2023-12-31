
def solution(file) :
	tc = 1
	while True :
		try :
			print("Tc : ", tc)	
			n = int(file.readline())
			scores = [int(file.readline()) for _ in range(n)]
			answer = int(file.readline())
			file.readline()

			print(n, scores, answer)

			count = 0
			scores.reverse()

			print(scores)

			for i in range(n-1) :
				if scores[i] <= scores[i+1] :
					print(scores[i], scores[i+1])
					count += scores[i+1] - scores[i] + 1
					scores[i+1] = scores[i] - 1
				print("scores : ", scores)
				print("count : ", count)

			print(count)
			print()

			tc += 1
				
		except :
			print("exception")
			break

# 백준 제출용
# n = int(input())
# scores = [int(input()) for _ in range(n)]
# scores.reverse()
# count = 0 

# for i in range(n-1) :
# 	if scores[i] <= scores[i+1] :
# 		count += scores[i+1] - scores[i] + 1
# 		scores[i+1] = scores[i] - 1
# print(count)

def main() :
	file = open("./그리디/게임을만든동준이tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()