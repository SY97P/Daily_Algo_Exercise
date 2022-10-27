def solution(file) : 
	for _ in range(4) : 
		n, m = map(int, file.readline().split())
		start = [list(list(file.readline().strip("\n"))) for _ in range(n)]
		end = [list(list(file.readline().strip("\n"))) for _ in range(n)]
		answer = int(file.readline())
		file.readline()

		# print(n, m, answer)
		# print("start list")
		# for s in start : 
		# 	print(s)
		# print("end list")
		# for e in end : 
		# 	print(e)

		count = 0 
		for i in range(n-2) : 
			for j in range(m-2) : 
				if start[i][j] != end[i][j] : 
					reverse(start, i, j)
					count += 1

		if check(start, end) : 
			print(count)
		else : 
			print(-1)
		# print()

# 백준 제출용
n, m = map(int, input().split())
start = [list(input().strip("\n")) for _ in range(n)]
end = [list(input().strip("\n")) for _ in range(n)]

count = 0 
for i in range(n-2) : 
	for j in range(m-2) : 
		if start[i][j] != end[i][j] : 
			reverse(start, i, j)
			count += 1
if check(start, end) : 
	print(count)
else : 
	print(-1)

def reverse(lst, row, col) : 
	for i in range(row, row + 3) :
		for j in range(col, col + 3) : 
			lst[i][j] = "0" if lst[i][j] == "1" else "1"
	# print("reversed list")
	# for l in lst : 
	# 	print(l)
	return lst

def check(lst1, lst2) :
	isSame = True
	for i in range(len(lst1)) : 
		if lst1[i] != lst2[i] : 
			isSame = False
	return isSame	

def main() : 
	file = open("./백준_그리디/행렬tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()

