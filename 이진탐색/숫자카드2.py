file = open("./이진탐색/숫자카드2tc.txt", "r")

n = int(file.readline())
nlist = list(map(int, file.readline().split()))
m = int(file.readline())
mlist = list(map(int, file.readline().split()))
answer = list(map(int, file.readline().split()))

print(n, nlist)
print(m, mlist)
print(answer)

# nlist를 dict{val : count} 로 변환
dic = {nl : 0 for nl in nlist}
for nl in nlist : 
	dic[nl] += 1

# for key in dic.keys() :
# 	print(key, dic[key])

keylist = list(dic.keys())
keylist.sort()

print(keylist)

for idx, ml in enumerate(mlist) : 
	# print(idx + 1, "번째 m ITEM")
	left, right = 0, len(keylist) - 1
	exist = False
	while left <= right : 
		mid = (left + right) // 2

		# print(keylist[mid], ml)
		# print(left, right)
	
		if keylist[mid] == ml : 
			exist = True
			break
		elif keylist[mid] < ml : 
			left = mid + 1
		else : 
			right = mid - 1

	if exist : 
		print(dic[ml], end = " ")
	else : 
		print(0, end = " ")
	

file.close()

# 백준 제출용
import sys

sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))
answer = list(map(int, sys.stdin.readline().split()))

dic = {nl : 0 for nl in nlist}
for nl in nlist : 
	dic[nl] += 1

keylist = list(dic.keys())
keylist.sort()

for ml in mlist : 
	# print(idx + 1, "번째 m ITEM")
	left, right = 0, len(keylist) - 1
	exist = False
	while left <= right : 
		mid = (left + right) // 2

		# print(keylist[mid], ml)
		# print(left, right)
	
		if keylist[mid] == ml : 
			exist = True
			break
		elif keylist[mid] < ml : 
			left = mid + 1
		else : 
			right = mid - 1

	if exist : 
		print(dic[ml], end = " ")
	else : 
		print(0, end = " ")
	