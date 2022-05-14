def solution(item) : 
	n, ropes, r = item
	answer = 0
	ropes = sorted(ropes)

	for i in range(n-1) :
		k = n - i
		weight = []
		for rope in ropes[i:] :
			weight.append(rope * k)
		answer = max(answer, min(weight))

	return answer

# 백준 제출용
n = int(input())
ropes = []
for i in range(n) : 
	ropes.append(int(input()))
answer = 0
ropes = sorted(ropes)

for i in range(n-1) :
	k = n - i
	weight = []
	for rope in ropes[i:] :
		weight.append(rope * k)
	answer = max(answer, min(weight))

print(answer) 
			

def main() : 
	tc = []
	file = open("./백준_그리디/로프tc.txt", "r")

	for i in range(2) :
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
