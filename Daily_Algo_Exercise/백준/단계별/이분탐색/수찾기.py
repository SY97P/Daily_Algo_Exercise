file = open("./이진탐색/수찾기tc.txt", "r")

n = int(file.readline())
nlist = list(map(int, file.readline().split()))
m = int(file.readline())
mlist = list(map(int, file.readline().split()))

file.readline()
answer = [int(file.readline()) for _ in range(m)]

nlist.sort()

print(n, nlist)
print(m, mlist)
print(answer)

def bin(item) : 
	left, right = 0, n-1

	while left < right : 
		med = (left + right) // 2

		print("nlist : ", item, med, nlist[med])
		
		if item < nlist[med] :
			right = med - 1
		else : 
			if item == nlist[med] : 
				return True
			left = med + 1
			
	return item == nlist[right]

for ml in mlist : 
	if bin(ml) : 
		print(1)
	else : 
		print(0)


file.close()

# 백준 제출용
# import sys

# n = int(sys.stdin.readline())
# nlist = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# mlist = list(map(int, sys.stdin.readline().split()))

# nlist.sort()

# def bin(item) : 
# 	left, right = 0, n-1

# 	while left < right : 
# 		med = (left + right) // 2
		
# 		if item < nlist[med] :
# 			right = med - 1
# 		else : 
# 			if item == nlist[med] : 
# 				return True
# 			left = med + 1
			
# 	return item == nlist[right]

# for ml in mlist : 
# 	if bin(ml) : 
# 		print(1)
# 	else : 
# 		print(0)
