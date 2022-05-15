# 모든 rope에 대해서 할 필요 없이 가장 작은 로프만 계산하면 됨. 

def solution(item) : 
	n, ropes, r = item
	answer = 0
	ropes = sorted(ropes)
	k = 1
	while ropes : 
		rope = ropes.pop()
		answer = max(answer, k * rope)
		# print("rope : ", rope, " k : ", k, " answer : ", answer)
		k += 1		

	return answer

# 백준 제출용
n = int(input())
answer, k = 0, 1
ropes = [int(input()) for i in range(n)]
ropes = sorted(ropes)

while ropes : 
	answer = max(answer, k * ropes.pop())
	k += 1
	
print(answer)
			

def main() : 
	tc = []
	file = open("./백준_그리디/로프tc.txt", "r")

	for i in range(3) :
		n = int(file.readline())
		rope = []
		for j in range(n) : 
			rope.append(int(file.readline()))
		r = int(file.readline())
		tc.append([n, rope, r])

	file.close()

	for item in tc : 
		print("solution : ", solution(item), " answer : ", item[2])

main()
