# 현재 도시와 다음 도시의 가격을 비교
# 현재 도시보다 작은 도시까지의 거리를 모두 더해감.
# 가격이 더 작은 도시에 도달하면 해당하는 여태까지 더한 거리를 모두 더해서
from collections import deque
def solution(item) : 
	n, distance, costs, _ = item
	distance = deque(distance)
	costs = deque(costs)

	# print(distance, costs)
	count, dist = 0, 0
	answer = 0
	while costs : 
		if count > 1 : 
			cost = costs.popleft()
			count -= 1
			continue
		cost = costs.popleft()
		count = 0
		dist = 0
		for i, c in enumerate(costs) : 
			try :
				dist += distance.popleft()
			
				# 더 작은 마을에 도착하면 그동안 쓸 주유금액을 모두 더해줌.
				if c < cost : 
					count = i+1
					answer += dist * cost
					break
			except : 
				print("dist : ", dist)
				answer += dist * cost
				break
		print("cost : ", cost, " dist : ", dist)
		print("answer : ", answer)
		
				
	return answer
		

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
		print("solution : ", solution(item), " answer : ", item[3])

main()