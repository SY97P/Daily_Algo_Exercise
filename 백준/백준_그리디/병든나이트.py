# 반복이나 재귀로 풀 수 있는 문제가 아니었음
# def move(coordi, key) :
# 	i, j = coordi
# 	# 2칸 위로, 1칸 오른쪽
# 	if key == 1 :
# 		return (i+2, j+1)
# 	# 1칸 위로, 2칸 오른쪽
# 	elif key == 2 :
# 		return (i+1, j+2)
# 	# 1칸 아래, 2칸 오른쪽
# 	elif key == 3 :
# 		return (i-1, j+2)
# 	# 2칸 아래, 1칸 오른쪽
# 	else :
# 		return (i-2, j+1)
		

# def solution(file) :
# 	for i in range(5) :
# 		n, m = map(int, file.readline().split())
# 		answer = int(file.readline())
# 		file.readline()

# 		print(n, m, answer)

# 		count = 1
# 		coordi = (0, 0)
# 		path = set([coordi])

# 		# 횡이동은 오른쪽 밖에 안되므로 무조건 세로 방향 (1,4) 이동 우선
# 		while coordi[0] + 2 < n and coordi[1] + 1 < m :
# 			coordi = move(coordi, 1)
# 			path.add(coordi)
# 		while coordi[0] - 2 < n and coordi[1] + 1 < m :
# 			coordi = move(coordi, 4)
# 			path.add(coordi)
# 		# 남은 공간 있으면 0에 가까운지 n에 가까운지에 따라
# 		# 반대 방향으로 이동하도록 유도
# 		if coordi[0] <= n//2 : # 0에 가까움
# 			while coordi[0] + 1 < n and coordi[1] + 2 < m :
# 				coordi = move(coordi, 2)
# 				path.add(coordi)
# 		else :
# 			while coordi[0] - 1 > 0 and coordi[1] + 2 < m :
# 				coordi = move(coordi, 3)
# 				path.add(coordi)

# 		print(len(path))
# 		print()
			

# 다른 방식으로 풀어야 한다.
def solution(file) :
	for _ in range(5) :
		n, m = map(int, file.readline().split())
		answer = int(file.readline())
		file.readline()

		print(n, m, answer)

		# 2칸 위로, 1칸 오른쪽
		# 1칸 위로, 2칸 오른쪽
		# 1칸 아래로, 2칸 오른쪽
		# 2칸 아래로, 1칸 오른쪽

		# 높이가 1이면 답은 위 or 아래 1개뿐
		if n == 1 :
			print(1)
		# 높이가 2이면 2칸 위아래 
		elif n == 2:
			print(min(4, (m+1) // 2))
		elif m <= 6 :
			print(min(4, m))
		else :
			print(m-2)
			

def main() :
	file = open("./백준_그리디/병든나이트tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
