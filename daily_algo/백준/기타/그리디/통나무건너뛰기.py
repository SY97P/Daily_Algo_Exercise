from collections import deque

file = open("./그리디/통나무건너뛰기tc.txt", "r")

tc = int(file.readline())
for t in range(tc) :
	# print(t + 1, "번째 테스트 케이스")
	n = int(file.readline())
	bulks = list(map(int, file.readline().split()))

	print(n, bulks)

	# 3번 해결방법 -> 정답
	# 2번 해결방법에서 시간초과만 해결하도록 수정
	bulks.sort()

	left_queue = deque([bulks[0]])
	right_queue= deque([bulks[1]])
	add_left = True

	for i in range(2, n) :
		if add_left :
			left_queue.append(bulks[i])
		else : 
			right_queue.appendleft(bulks[i])
		add_left = not add_left
	print(left_queue, right_queue)
	queue = left_queue + right_queue
	lst = [abs(queue[i] - queue[i-1]) for i in range(1, n)]
	print(max(lst))
	print()

	# # 2번 해결방법 -> 시간초과
	# # 1. 정렬
	# # 2. [1st, 2nd]
	# # 3. [1st, 3rd, 2nd]
	# # 4. [1st, 3rd, 4th, 2nd]
	# # 5. [1st, 3rd, 5th, 4th, 2nd] ...
	# # index 필요
	# bulks.sort()

	# index = 2
	# queue = [bulks[0], bulks[2], bulks[1]]
	# is_plus = False

	# for i in range(3, n) : 
	# 	queue = queue[:index] + [bulks[i]] + queue[index:]
	# 	if is_plus :
	# 		index += 1
	# 		is_plus = False
	# 		continue
	# 	is_plus = True
	# print(queue)
	# lst = [abs(queue[i] - queue[i-1]) for i in range(1, n)]
	# print(max(lst))
	# print()


	# # 1번 해결방법 -> 알고리즘 폐기
	# # 최소, 최대값을 정해두고
	# # 최소에 가까우면 최소값 뒤에, 최대에 가까우면 최대값뒤에
	# # 마지막 값은 맨 뒤에 붙여서 정답 구하기
	# bulks.sort()

	# minValue, maxValue = bulks[0], bulks[-1]
	# queue = [minValue, maxValue]
	# minDuple, maxDuple = False, False

	# for i in range(n-2, 1, -1) : 
	# 	# print("current bulk is ", bulks[i])
	# 	min_diff, max_diff = bulks[i] - minValue, maxValue - bulks[i]
	# 	# print("min_diff, max_diff", min_diff, max_diff)
	# 	if min_diff > max_diff : # 최대값에 더 가까우면 최대 뒤에 붙임
	# 		# print("maxDuple is ", maxDuple)
	# 		if maxDuple :
	# 			# 최소값 뒤에 붙임
	# 			maxDuple = False
	# 			queue = [minValue, bulks[i]] + queue[1:]
	# 			# print("maxDuple is changed into ", maxDuple)
	# 			# print("queue : ", queue)
	# 			# print()
	# 			continue
	# 		queue.append(bulks[i])
	# 		maxDuple = True
	# 	else : 
	# 		# print("minDuple is ", minDuple)
	# 		if minDuple :
	# 			minDuple = False
	# 			queue.append(bulks[i])
	# 			# print("queue : ", queue)
	# 			# print()
	# 			continue
	# 		queue = [minValue, bulks[i]] + queue[1:]
	# 		minDuple = True
	# 	# print("queue : ", queue)
	# 	# print()
	# # 두 번째로 작은 값은 맨 마지막에 붙임
	# queue.append(bulks[1])

	# print(queue)

	# # print([abs(queue[i] - queue[i-1]) for i in range(1, n)])
	# lst = [abs(queue[i] - queue[i-1]) for i in range(1, n)]
	# print(max(lst))

	# print()

file.readline()

for t in range(tc) :
	print(t + 1, "번째 테스트 케이스 정답 : ", file.readline())

file.close()

# 백준 제출용
# tc = int(input())
# for _ in range(tc) : 
# 	n = int(input())
# 	bulks = list(map(int, input().split()))

# 	bulks.sort()

# 	left_queue = deque([bulks[0]])
# 	right_queue= deque([bulks[1]])
# 	add_left = True

# 	for i in range(2, n) :
# 		if add_left :
# 			left_queue.append(bulks[i])
# 		else : 
# 			right_queue.appendleft(bulks[i])
# 		add_left = not add_left
# 	# print(left_queue, right_queue)
# 	queue = left_queue + right_queue
# 	lst = [abs(queue[i] - queue[i-1]) for i in range(1, n)]
# 	print(max(lst))