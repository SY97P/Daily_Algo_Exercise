def solution(item) : 
	cost, count = item 
	answer = 0
	cost = 1000 - cost

	answer += cost // 500
	cost %= 500
	# print("500 answer : ", answer, " cost : ", cost)

	answer += cost // 100
	cost %= 100
	# print("100 answer : ", answer, " cost : ", cost)

	answer += cost // 50
	cost %= 50
	# print("50  answer : ", answer, " cost : ", cost)

	answer += cost // 10
	cost %= 10
	# print("10  answer : ", answer, " cost : ", cost)

	answer += cost // 5
	cost %= 5
	# print("5   answer : ", answer, " cost : ", cost)

	answer += cost // 1
	cost %= 1
	# print("1   answer : ", answer, " cost : ", cost)

	return answer

# 백준 제출용
cost = 1000 - int(input())
answer = 0
answer += cost // 500
cost %= 500

answer += cost // 100
cost %= 100

answer += cost // 50
cost %= 50

answer += cost // 10
cost %= 10

answer += cost // 5
cost %= 5

answer += cost // 1
cost %= 1

print(answer)

def main() : 
	file = open("./백준_그리디/거스름돈tc.txt", "r")
	
	for i in range(2) : 
		print("solution : ", solution(map(int, file.readline().split())))
	
	file.close()

main()
