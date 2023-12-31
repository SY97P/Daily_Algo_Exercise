def solution(file) : 
	for _ in range(6) :
		n, m = map(int, file.readline().split())
		values = []
		# [6패키지, 낱개]
		for _ in range(m) :
			values.append(list(map(int, file.readline().split())))
		answer = int(file.readline())
		file.readline()

		print(n, m, values, answer)

		# 고려대상
		# 각 브랜드별로 패키지랑 낱개 중에 가성비 좋은 걸 택해서 기록
		# 가성비 별로 정렬해서 n이랑 6이랑 비교
		# n이 6보다 크면 패키지 먼저 잡숫게 하고
		# n이 6보다 작으면 낱개를 먼저 잡숫게 함
		# package_values.pop(0)[0], indi_values.pop(0)[1] * (n-curr_count)

		curr_value = 0
			
		package_values = sorted(values)
		indi_values = sorted(values, key = lambda x: x[1])

		# 패키지가 더 싸면
		if package_values[0][0] < indi_values[0][1] * 6 : 
			curr_value = package_values[0][0] * (n // 6)
			if package_values[0][0] < indi_values[0][1] * (n % 6) :
				curr_value += package_values[0][0]
			else : 
				curr_value += indi_values[0][1] * (n % 6)
		else : 
			curr_value = indi_values[0][1] * (n % 6)
			
		print(curr_value)

# 백준 제출용
# n, m = map(int, input().split())
# values = []
# for _ in range(m) : 
# 	values.append(list(map(int, input().split())))
# curr_value = 0
# package_values = sorted(values, key = lambda x : x[0])
# indi_values = sorted(values, key = lambda x: x[1])

# if package_values[0][0] < indi_values[0][1] * 6 : 
# 	curr_value = package_values[0][0] * (n // 6)
# 	if package_values[0][0] < indi_values[0][1] * (n % 6) :
# 		curr_value += package_values[0][0]
# 	else : 
# 		curr_value += indi_values[0][1] * (n % 6)
# else :
# 	curr_value = indi_values[0][1] * n
			
# print(curr_value)

def main() :
	file = open("./그리디/기타줄tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()