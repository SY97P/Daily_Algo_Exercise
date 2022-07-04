from collections import deque

def solution(file) :
	for _ in range(5) :
		n, k = map(int, file.readline().split())
		token = deque(list(file.readline().rstrip("\n")))
		answer = int(file.readline())
		file.readline()
   
		print(n, k, token, answer)

		count = 0
		queue = deque([])
		while count < k :
			if not token :
				while len(queue) > n - k :
					queue.pop()
				break
			curr = token.popleft()
			# print(curr)
			if not queue :
				queue.append(curr)
				continue
			# 현재 값보다 작은 큐이 값은 k 범위내에서 제거해감
			while queue and count < k and curr > queue[-1] :
				queue.pop()
				count += 1
			queue.append(curr)
			# print(queue, count)
		print(int(''.join(queue + token)))

# 백준 제출용
# from collections import deque
# n, k = map(int, input().split())
# token = deque(list(input().strip('\n')))
# count = 0
# queue = deque([])
# while count < k :
# 	if not token :
# 		while len(queue) < n-k :
# 			queue.pop()
# 		break
# 	curr = token.popleft()
# 	if not queue :
# 		queue.append(curr)
# 		continue
# 	while queue and count < k and curr > queue[-1] :
# 		count += 1
# 		queue.pop()
# 	queue.append(curr)
# print(int(''.join(queue + token)))
				

def main() :
	file = open("./백준_그리디/크게만들기tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
