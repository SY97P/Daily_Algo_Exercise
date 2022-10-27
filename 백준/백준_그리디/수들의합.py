def solution(item) : 
	s, n = item

	answer = 0
	sum, factor = 0, 1

	while sum < s : 
		sum += factor
		answer += 1
		factor += 1

	return answer if sum <= s else answer - 1

# 백준 제출용
s = int(input())
answer, sum, factor = 0, 0, 1

while sum < s : 
	sum += factor 
	answer += 1
	factor += 1

print(answer if sum <= s else answer - 1)

def main() : 
	tc = []

	file = open("./백준_그리디/수들의합tc.txt", "r")

	for i in range(1) : 
		s, n = int(file.readline()), int(file.readline())
		tc.append([s,n])
	
	file.close()

	for item in tc : 
		print("solution : ", solution(item))

main()