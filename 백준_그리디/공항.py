def checkPlane(queue, index) :
	temp = index - 1
	while queue[temp] == 0 :
		if temp < 0 :
			break
		temp -= 1
	if temp < 0 :
		# 이전 값 중에 0이 아닌 값이 없는것
		# 현재 인덱스 + 1 보다 큰 값이 있는거 아니면 참 반환
		if index + 1 < queue[index] :
			return False
		else :
			return True
	else :
		# 이전 값 중 0인 값이 있음 (temp 인덱스 값)
		# 해당 값이랑 비교해서 index의 값이 index - temp 보다 크면 거짓 반환
		if queue[index] > index - temp :
			return False
		else :
			return True
			
	

def solution(file) :
	for _ in range(2) :
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

		queue = [0 for _ in range(g)]
		count = 0
		for pl in planes :
			queue[pl-1] += 1
			if checkPlane(queue, pl-1) : 
				count += 1
			else : 
				break
		print(count)
			

# 백준 제출용
import sys

def checkPlane(queue, index) :
	temp = index - 1
	while queue[temp] == 0 :
		if temp < 0 :
			break
		temp -= 1
	if temp < 0 :
		# 이전 값 중에 0이 아닌 값이 없는것
		# 현재 인덱스 + 1 보다 큰 값이 있는거 아니면 참 반환
		if index + 1 < queue[index] :
			return False
		else :
			return True
	else :
		# 이전 값 중 0인 값이 있음 (temp 인덱스 값)
		# 해당 값이랑 비교해서 index의 값이 index - temp 보다 크면 거짓 반환
		if queue[index] > index - temp :
			return False
		else :
			return True
			
g = int(sys.stdin.readline().strip('\n'))
p = int(sys.stdin.readline().strip('\n'))
planes = [int(sys.stdin.readline().strip('\n')) for _ in range(p)]

queue = [0 for _ in range(g)]
count = 0 

for pl in planes :
	queue[pl-1] += 1
	if checkPlane(queue, pl - 1) :
		count += 1
	else :
		break
print(count)

def main() :
	file = open("./백준_그리디/공항tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
