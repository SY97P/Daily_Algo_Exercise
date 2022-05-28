def solution(n, item) : 
	print(n, item)
	answer = 1

	item = sorted(item,  key = lambda x : x[0])

	first = item.pop(0)
	interview = first[1]

	while item : 
		_, curr = item.pop(0)
		if curr < interview : 
			answer += 1
			interview = curr

	return answer

# 백준 제출용
import sys
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
nominees = []
answer = 0
for i in range(n) : 
	nominees.append(sys.stdine)
first = nominees.pop(0)
interview = first[1]
while nominees : 
	_, curr = nominees.pop(0)
	if curr < interview : 
		answer += 1
		interview = curr

print(answer)
		

def main() : 
	file = open("./백준_그리디/신입사원tc.txt", "r")

	t = int(file.readline())
	for i in range(t) : 
		n = int(file.readline())
		tc = []
		for j in range(n) : 
			tc.append(list(map(int, file.readline().split())))
		print("solution : ", solution(n, tc))

main()