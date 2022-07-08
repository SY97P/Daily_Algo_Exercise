<<<<<<< HEAD
# def checkPlane(queue, index) :
# 	temp = index - 1
# 	while temp >= 0 and queue[temp] == 0 :
# 		temp -= 1
# 	if temp < 0 :
# 		# 이전 값 중에 0이 아닌 값이 없는것# 
# 		# 현재 인덱스 + 1 보다 큰 값이 있는거 아니면 참 반환
# 		if index + 1 < queue[index] :
# 			return False
# 		else :
# 			return True
# 	else :
# 		# 이전 값 중 0인 값이 있음 (temp 인덱스 값)
# 		# 해당 값이랑 비교해서 index의 값이 index # - temp 보다 크면 거짓 반환
# 		if queue[index] > index - temp :
# 			return False
# 		else :
# 			return True

def find_parent(dic, x) :
	if dic[x] == x :
		return x
	value = find_parent(parent[x])
	parent[x] = value
	

def solution(file) :
	for _ in range(4) :
		g = int(file.readline().strip('\n'))
		p = int(file.readline().strip('\n'))
		planes = [int(file.readline().strip('\n')) for _ in range(p)]
		answer = int(file.readline().strip('\n'))
		file.readline()

		print(g, p, planes, answer)

		# gates = [False for _ in range(g)]
		# count = 0

		# for pl in planes :
		# 	try :
		# 		# reversed list 는 reverse_iterator 객체를 반환
		# 		# 해당 객체는 index 라이브러리가 없음
		# 		# 이런식으로 list type으로 형변환을 해줘야 함
		# 		lst = list(reversed(gates[:pl]))
		# 		index = lst.index(False)
		# 		gates[pl-1-index] = True
		# 		count += 1
		# 	except :
		# 		break

		# 시간초과 해결 방안
		# 이렇게 하면 틀리다고 나음.
		# queue = [0 for _ in range(g)]
		# count = 0
		# for pl in planes :
		# 	queue[pl-1] += 1
		# 	if checkPlane(queue, pl-1) : 
		# 		count += 1
		# 	else : 
		# 		break
		# print(count)

		# union-find algorithm
		parent = {i : i for i in range(g+1)}
		count = 0

		for pl in planes :
			# 현재 비행기의 부모를 구함
			# 구한 부모가 0보다 작거나 같으면 폐쇄조건
			# 그렇지 않으면 count 를 증가해주면 된다.s
			value = find_parent(pl)

			if value <= 0 :
				break
			union(value , value - 1)
			count += 1
		print(count)

# 백준 제출용

=======
# 아예 새로
# 전역변수 쓰고 싶음

def find_parent(x) :
	if parent[x] == x :
		return x
	P = find_parent(parent[x])
	parent[x] = P
	return parent[x]

def union(x, y) :
	x = find_parent(x)
	y = find_parent(y)
	if x < y :
		parent[y] = x
	else :
		parent[x] = y

file = open("./백준_그리디/공항tc.txt", "r")

for _ in range(2) :
	g = int(file.readline().strip("\n"))
	p = int(file.readline().strip("\n"))
	planes = [int(file.readline().strip("\n")) for _ in range(p)]
	answer = int(file.readline().strip("\n"))
	file.readline()

	print(g, p, planes, answer)

	parent = {i : i for i in range(g+1)}
	count = 0 

	for pl in planes : 
		if find_parent(pl) == 0 :
			break
		union(pl, pl - 1)
		count += 1
	print(count)

file.close()



# # def checkPlane(queue, index) :
# # 	temp = index - 1
# # 	while queue[temp] == 0 :
# # 		if temp < 0 :
# # 			break
# # 		temp -= 1
# # 	if temp < 0 :
# # 		# 이전 값 중에 0이 아닌 값이 없는것
# # 		# 현재 인덱스 + 1 보다 큰 값이 있는거 아니면 참 반환
# # 		if index + 1 < queue[index] :
# # 			return False
# # 		else :
# # 			return True
# # 	else :
# # 		# 이전 값 중 0인 값이 있음 (temp 인덱스 값)
# # 		# 해당 값이랑 비교해서 index의 값이 index - temp 보다 크면 거짓 반환
# # 		if queue[index] > index - temp :
# # 			return False
# # 		else :
# # 			return True

# # dict에서 해당 x에 대한 부모를 계속 타고 들어가서 최종 부모의 값을 가져옴
# def find_parent(parent, x) :
# 	# 종료조건
# 	# 현재 값과 부모의 값이 같으면 아직 들어갈 공간이 남았다는 것
# 	if parent[x] == x :
# 		return x
# 	# 부모를 통해서 받아온 값을 넣어줌
# 	P = find_parent(parent, parent[x])
# 	parent[x] = P
# 	return parent[x]

# def union(parent, x, y) :
# 	x = find_parent(parent, x)
# 	y = find_parent(parent, y)
# 	if x < y :
# 		parent[y] = x
# 	else : 
# 		parent[x] = y

# def solution(file) :
# 	for _ in range(2) :
# 		g = int(file.readline().strip('\n'))
# 		p = int(file.readline().strip('\n'))
# 		planes = [int(file.readline().strip('\n')) for _ in range(p)]
# 		answer = int(file.readline().strip('\n'))
# 		file.readline()

# 		print(g, p, planes, answer)

# 		# gates = [False for _ in range(g)]
# 		# count = 0

# 		# for pl in planes :
# 		# 	try :
# 		# 		# reversed list 는 reverse_iterator 객체를 반환
# 		# 		# 해당 객체는 index 라이브러리가 없음
# 		# 		# 이런식으로 list type으로 형변환을 해줘야 함
# 		# 		lst = list(reversed(gates[:pl]))
# 		# 		index = lst.index(False)
# 		# 		gates[pl-1-index] = True
# 		# 		count += 1
# 		# 	except :
# 		# 		break

# 		# 시간초과 해결 방안
# 		# 이 방법은 오답 발생
# 		# queue = [0 for _ in range(g)]
# 		# count = 0
# 		# for pl in planes :
# 		# 	queue[pl-1] += 1
# 		# 	if checkPlane(queue, pl-1) : 
# 		# 		count += 1
# 		# 	else : 
# 		# 		break
# 		# print(count)

# 		# union-find 알고리즘 사용
# 		parent = {i : i for i in range(g)}
# 		count = 0

# 		for pl in planes : 
# 			x = find_parent(parent, pl)

# 			if x == 0 :
# 				break
# 			union(parent, x, x - 1)
# 			count += 1
# 		print(count)
			

# # 백준 제출용
# # import sys

# # def checkPlane(queue, index) :
# # 	temp = index - 1
# # 	while queue[temp] == 0 :
# # 		if temp < 0 :
# # 			break
# # 		temp -= 1
# # 	if temp < 0 :
# # 		# 이전 값 중에 0이 아닌 값이 없는것
# # 		# 현재 인덱스 + 1 보다 큰 값이 있는거 아니면 참 반환
# # 		if index + 1 < queue[index] :
# # 			return False
# # 		else :
# # 			return True
# # 	else :
# # 		# 이전 값 중 0인 값이 있음 (temp 인덱스 값)
# # 		# 해당 값이랑 비교해서 index의 값이 index - temp 보다 크면 거짓 반환
# # 		if queue[index] > index - temp :
# # 			return False
# # 		else :
# # 			return True
			
# # g = int(sys.stdin.readline().strip('\n'))
# # p = int(sys.stdin.readline().strip('\n'))
# # planes = [int(sys.stdin.readline().strip('\n')) for _ in range(p)]

# # queue = [0 for _ in range(g)]
# # count = 0 

# # for pl in planes :
# # 	queue[pl-1] += 1
# # 	if checkPlane(queue, pl - 1) :
# # 		count += 1
# # 	else :
# # 		break
# # print(count)
>>>>>>> 108997e6663a7a302df30f2f795fbc7d79117940

# def main() :
# 	file = open("./백준_그리디/공항tc.txt", "r")
# 	print("solution : ", solution(file))
# 	file.close()

# main()
