# 해결방법 3번 :
# BFS로 풀어야 해
# 해결방법 1이 메모리 에러가 났으니까 이를 해결
# 이동해서 얻은 값이 k보다 2배 크면 버리는 걸로 하자
from collections import deque

def bfs(queue) : 
	while queue : 
		curr, count = queue.popleft()

		print(curr, count, queue)

		# 종료조건
		if curr == k : 
			return count

		# k보다 2배 큰 건 버림
		# 후보군 생성과 동시에 검사하자
		# k < n 일 가능성을 고려하지 않았음.
		for can in [curr * 2, curr + 1, curr - 1] :
			print(can, end = " ")
			if can == k :
				return count + 1
			if can not in number_set and lower_bound <= can <= upper_bound : 
				number_set.add(can)
				queue.append((can, count + 1))
		print()
		

file = open("./bfs/숨바꼭질tc.txt", "r")

for tc in range(4) : 
	n, k = map(int, file.readline().split())
	answer = int(file.readline())
	file.readline()

	if k < n :
		print(n - k)
	else : 
		lower_bound, upper_bound = 0, k * 25
		number_set = set([n])
		
		print(n, k, answer)
	
		print("result : ", bfs(deque([(n, 0)])))

file.close()

# 백준 제출용
# from collections import deque

# def bfs(queue) : 
# 	while queue : 
# 		curr, count = queue.popleft()

# 		# 종료조건
# 		if curr == k : 
# 			return count

# 		# k보다 2배 큰 건 버림
# 		# 후보군 생성과 동시에 검사
# 		for can in [curr * 2, curr + 1, curr - 1] :
# 			if can == k : 
# 				return count + 1
# 			if can not in number_set and lower_bound < can < upper_bound : 
# 				number_set.add(can)
# 				queue.append((can, count + 1))
		

# n, k = map(int, input().split())
# if k < n :
# 	print(n - k)
# else :
# 	lower_bound, upper_bound = 0, k*25
# 	number_set = set([n])
# 	print(bfs(deque([(n, 0)])))


# # 해결방법 2번 : DFS 한계 때문에 안 됨
# # 우선순위 적용 DFS
# file = open("./bfs/숨바꼭질tc.txt", "r")

# def dfs(curr, count) : 
# 	if curr == k :
# 		return count

# 	candi = [curr * 2, curr - 1, curr + 1]
# 	candi.sort(key = lambda x: abs(k - x))
# 	print(candi, count+1)
	
# 	for c in candi : 
# 		return dfs(c, count + 1)


# n, k = map(int, file.readline().split())
# answer = int(file.readline())
# file.readline()

# print(n, k, answer)

# result = dfs(n, 0)

# print(result)

# file.close()


# 해결방법 1번 : 메모리 초과 
# 무지성 BFS
# from collections import deque

# file = open("./bfs/숨바꼭질tc.txt", "r")

# def bfs(queue) :
# 	while queue : 
# 		curr, count = queue.popleft()

# 		if curr == k :
# 			break

# 		queue.append((curr * 2, count + 1))
# 		queue.append((curr - 1, count + 1))
# 		queue.append((curr + 1, count + 1))

# 	return count
	

# for _ in range(1) : 
# 	n, k = map(int, file.readline().split())
# 	answer = int(file.readline())
# 	file.readline()

# 	print(n, k, answer)

# 	result = bfs(deque([(n, 0)]))

# 	print(result)

# file.close()

# # 백준 제출용
# from collections import deque

# def bfs(queue) :
# 	while queue : 
# 		curr, count = queue.popleft()

# 		if curr == k :
# 			break

# 		queue.append((curr * 2, count + 1))
# 		queue.append((curr - 1, count + 1))
# 		queue.append((curr + 1, count + 1))

# 	return count
	
# n, k = map(int, input().split())
# result = bfs(deque([(n, 0)]))
# print(result)
