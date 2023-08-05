def solution(item) : 
	n, distance, costs, answer = item

	min_cost = costs[0]
	answer = 0

	for i in range(n-1) : 
		if min_cost > costs[i] : 
			min_cost = costs[i]
		
		answer += min_cost * distance[i]
		print(min_cost, distance[i], answer)

	return answer

# 백준 제출용
n = int(input())
distance = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost, answer = costs[0], 0

for i in range(n-1) : 
	if min_cost > costs[i] : 
		min_cost = costs[i]
	answer += min_cost * distance[i]
print(answer)

def main() : 
	tc = []
	file = open("./그리디/주유소tc.txt", "r")

	for i in range(5) : 
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


# 이렇게 풀면 부분점수 나옴.
# # 현재 도시와 다음 도시의 가격을 비교
# # 현재 도시보다 작은 도시까지의 거리를 모두 더해감.
# # 가격이 더 작은 도시에 도달하면 해당하는 여태까지 더한 거리를 모두 더해서
# from collections import deque
# def solution(item) : 
# 	n, distance, costs, answer = item 
# 	distance = deque(distance)
# 	costs = deque(costs)

# 	answer = 0
# 	dist = 0
# 	cost = costs.popleft()
# 	while costs : 
# 		next = costs.popleft()
# 		if not costs : 
# 			dist += distance.popleft()
# 			answer += cost * dist
# 		else :
# 			if cost < next : 
# 				dist += distance.popleft()
# 			else : 
# 				dist = dist if dist != 0 else distance.popleft()
# 				answer += (cost * dist)
# 				cost = next
# 				dist = 0
# 		# print(cost, next, dist, answer)
# 	return answer

# # 백준 제출용
# # from collections import deque
# # n = int(input())
# # distance = deque(list(map(int, input().split())))
# # costs = deque(list(map(int, input().split())))

# # answer, dist, cost = 0, 0, costs.popleft()
# # while costs : 
# # 	next = costs.popleft()
# # 	if not costs : 
# # 		dist += distance.popleft()
# # 		answer += cost * dist
# # 	else : 
# # 		if cost < next : 
# # 			dist += distance.popleft()
# # 		else : 
# # 			dist = dist if dist != 0 else distance.popleft()
# # 			answer += (cost * dist)
# # 			cost = next
# # 			dist = 0
# # print(answer)