#1 6
#2 8
#3 7
#4 6
#5 10
#6 7
#7 -1
#8 11
#9 8
#10 4
#11 4
#12 -1
#13 6
#14 9
#15 2
#16 5
#17 -1
#18 4
#19 5
#20 9
#21 7
#22 2
#23 10
#24 9
#25 5
#26 6
#27 6
#28 15
#29 3
#30 -1
#31 5
#32 5
#33 4
#34 6
#35 6
#36 2
#37 2
#38 8
#39 8
#40 -1
#41 5
#42 9
#43 7
#44 2
#45 7
#46 5
#47 7
#48 8
#49 5
#50 5
#51 7
#52 7
#53 6
#54 2
#55 7
#56 6
#57 5
#58 7
#59 7
#60 6
#61 9
#62 7
#63 7
#64 7
#65 6
#66 11
#67 5
#68 12
#69 9
#70 6
#71 5
#72 7
#73 7
#74 5
#75 -1
#76 7
#77 6
#78 2
#79 5
#80 6
#81 -1
#82 -1
#83 -1
#84 2
#85 6
#86 11
#87 -1
#88 7
#89 7
#90 10
#91 7
#92 9
#93 2
#94 7
#95 9
#96 5
#97 7
#98 6
#99 6
#100 4

file = open("./SWEA/D4/지희의고장난계산기.txt", "r")

input = file.readline

import math

t = int(input())

def dfs(target) : 
	count = check(target)

	# 목표 숫자 패드 조합 가능
	if count != -1 : 
		return count

	result = float('inf')

	# 목표 숫자 패드 조합 불가 -> 약분
	for i in range(2, int(math.sqrt(target)) + 1) :
		if target % i == 0 : 
			div_count = check(i)

			if div_count != -1 : 
				# 곱셈 버튼 추가 
				div_count += 1 
				# 나뉜 숫자를 다시 판별
				div_result = dfs(target // i)

				if div_result != float('inf') : 
					result = min(result, div_count + div_result)

	return result
				
def check(target) : 
	count = 0
	temp = target

	while temp >= 10 : 
		if keypad[temp%10] == 0 : 
			count = -1
			break
		temp //= 10
		count += 1

	count += 1
	if keypad[temp%10] == 0 : 
		count = -1

	return count
		

for tc in range(1, t + 1) : 
	keypad = list(map(int, input().split()))
	target = int(input())

	# if tc != 1 : 
	# 	continue

	result = dfs(target)

	print("#%d %d" %(tc, -1 if result == float('inf') else result + 1))


file.close()