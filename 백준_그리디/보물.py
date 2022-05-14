def solution(item) : 
	answer = 0
	n, a, b, r = item 

	# 곱한 결과가 가장 작게 만드는 법
	# 최대한 큰 수 랑 최대한 작은 수가 곱해지면 됨. 
	# b를 정렬한 다음 서로 결합할 a 애들을 dict으로 만들어서 둠. 
	# 나중에 오리지널 b랑 비교해서 배열하면 될 듯
	
	temp_b = sorted(b)
	temp_a = sorted(a, reverse = True)
	print(temp_b, temp_a)

	for i, v in enumerate(temp_b) : 
		answer += v * temp_a[i]

	return answer


# 백준 제출용
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# answer = 0 

# temp_a = sorted(a)
# temp_b = sorted(b, reverse = True)

# for i, v in enumerate(temp_b) :
# 	answer += v * temp_a[i]

# print(answer)
	

def main() : 
	tc = []
	file = open("./백준_그리디/보물TC.txt", 'r')
	for _ in range(3) : 
		n = int(file.readline())
		a = list(map(int, file.readline().split()))
		b = list(map(int, file.readline().split()))
		r = int(file.readline())
		tc.append([n, a, b, r])
	# print(tc)
	file.close()

	for item in tc : 
		print("solution : ", solution(item), " answer : ", item[3])

main()

