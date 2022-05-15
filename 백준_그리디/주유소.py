# 현재 도시와 다음 도시의 가격을 비교
# 현재 도시보다 작은 도시까지의 거리를 모두 더해감.
# 가격이 더 작은 도시에 도달하면 해당하는 여태까지 더한 거리를 모두 더해서
def solution(item) : 
	n, distance, costs, answer = item

	

def main() : 
	tc = []
	file = open("./백준_그리디/주유소tc.txt", "r")

	for i in range(2) : 
		n = int(file.readline())
		distance = list(map(int,file.readline().split()))
		costs = list(map(int, file.readline().split()))
		answer = int(file.readline())
		tc.append([n, distance, costs, answer])

		
	file.close()
	# print(tc)

	for item in tc : 
		print("solution : ", solution(item))

main()