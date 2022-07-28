file = open("./백준_그리디/주사위tc.txt", "r")

for _ in range(4) : 
	n = int(file.readline())
	dice = list(map(int, file.readline().split()))
	answer = int(file.readline())
	file.readline()

	print(n, answer)
	print(dice)

	# 각각 마주보는 면 중에서 작은 값 (보여줄 값)을 구함
	min_list = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
	print(min_list)

	min_list.sort()

	# 보여지는 면에 따라 해당 주사위가 보여주어야 할 값
	one_plate = min_list[0]
	two_plate = sum(min_list[:2])
	thr_plate = sum(min_list)

	# 보여지는 면에 따른 주사위 개수
	one_count = 4 * (n-2) * (n-1) + (n-2) ** 2
	two_count = 4 * (n-1) + 4 * (n-2)
	thr_count = 4

	answer = one_plate * one_count + two_plate * two_count + thr_plate * thr_count

	print(answer)

	print()

file.close()