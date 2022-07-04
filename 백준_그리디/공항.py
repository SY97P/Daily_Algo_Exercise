

def solution(file) :
	for _ in range(2) :
		g = int(file.readline().strip('\n'))
		p = int(file.readline().strip('\n'))
		planes = [int(file.readline().strip('\n')) for _ in range(p)]
		answer = int(file.readline().strip('\n'))
		file.readline()

		print(g, p, planes, answer)

		gates = [False for _ in range(g)]
		count = 0

		for pl in planes :
			try :
				# reversed list 는 reverse_iterator 객체를 반환
				# 해당 객체는 index 라이브러리가 없음
				# 이런식으로 list type으로 형변환을 해줘야 함
				lst = list(reversed(gates[:pl]))
				index = lst.index(False)
				gates[pl-1-index] = True
				count += 1
			except :
				break
		print(count)
			

# # 백준 제출용
import sys

g = int(sys.stdin.readline().strip('\n'))
p = int(sys.stdin.readline().strip('\n'))
planes = [int(sys.stdin.readline().strip('\n')) for _ in range(p)]
gates = [False for _ in range(g)]
count = 0

for pl in planes :
	try :
		# reversed list 는 reverse_iterator 객체를 반환
		# 해당 객체는 index 라이브러리가 없음
		# 이런식으로 list type으로 형변환을 해줘야 함
		lst = list(reversed(gates[:pl]))
		index = lst.index(False)
		gates[pl-1-index] = True
		count += 1
	except :
		break
print(count)


def main() :
	file = open("./백준_그리디/공항tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
