from itertools import permutations
def solution(item) : 
	given, answer = item

	if given == 30 : 
		return 30
	elif given < 30 : 
		return -1

	nums = map(''.join , permutations(sorted(str(given), reverse = True), len(str(given))))
	for n in nums : 
		if int(n) % 30 == 0 :
			return int(n)
	return -1

# 백준 제출용
from itertools import permutations
given = input()
if int(given) == 30 : 
	print(30)
elif int(given) < 30 : 
	print(-1)
nums = map(''.join, permutations(sorted(given, reverse = True), len(given)))
for n in nums : 
	if int(n) % 30 == 0 :
		print(int(n))
		break
print(-1)

	

def main() : 
	tc = []
	file = open("./백준_그리디/30tc.txt", "r")
	for i in range(4) :
		tc.append(list(map(int, file.readline().split())))
	file.close()

	for item in tc :
		print("solution : ", solution(item), "\t\tanswer : ", item[1])

main()