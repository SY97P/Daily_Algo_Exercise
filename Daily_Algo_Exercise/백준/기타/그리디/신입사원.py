import sys
def solution(n, item) : 
	# print(n, item)
	# answer = 1

	# item = sorted(item,  key = lambda x : x[0])

	# first = item.pop(0)
	# interview = first[1]

	# while item : 
	# 	_, curr = item.pop(0)
	# 	if curr < interview : 
	# 		answer += 1
	# 		interview = curr
	
	

# 백준 제출용
# import sys
# for _ in range(int(sys.stdin.readline())) :
#     n = int(input())
#     nomi, answer = [], 1
#     for i in range(n) : 
#         nomi.append(list(map(int, sys.stdin.realine().strip().split())))
#     nomi = sorted(nomi)
#     interview = nomi[0][1]
#     for i in range(1, n) : 
#         if nomi[i][1] < interview : 
#             interview = nomi[i][1]
#             answer += 1
#     print(answer)
		

def main() : 
	file = open("./그리디/신입사원tc.txt", "r")

	t = int(file.readline())
	for i in range(t) : 
		n = int(file.readline())
		tc = []
		for j in range(n) : 
			tc.append(list(map(int, file.readline().split())))
		print("solution : ", solution(n, tc))

main()