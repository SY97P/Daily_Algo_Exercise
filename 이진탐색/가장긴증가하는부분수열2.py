file = open("./이진탐색/가장긴증가하는부분수열2tc.txt", "r")

for tc in range(1) : 
	n = int(file.readline())
	nlist = list(map(int, file.readline().split()))
	answer = int(file.readline())
	
	print(n, answer)
	print(nlist)
	
	nset = sorted(list(set(nlist)))
	print(nset)
	
	def getlen(index) : 
		curr = nlist[index]
		count = 1
		for i in range(index + 1, n) :
			if curr < nlist[i] :
				count += 1
				curr = nlist[i]
		return count
		
	
	left, right = 0, len(nset)
	maxlen = 0
	while left <= right : 
		mid = (left + right) // 2
	
		# 해당 좌표로 수열 만들기
		count = 0
		for i, nl in enumerate(nlist) : 
			if nset[mid] == nl : 
				temp = getlen(i)
				print("시작값 , 길이 : ", nl, temp)
				if count < temp :
					count = temp
	
		# 크네
		if count > maxlen : 
			right = mid - 1
			maxlen = count
		else : 
			left = mid + 1
	
	print(maxlen)
	

file.close()

# 백준 제출용
import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

nset = sorted(list(set(nlist)))
print(nset)

def getlen(index) : 
	curr = nlist[index]
	count = 1
	for i in range(index + 1, n) :
		if curr < nlist[i] :
			count += 1
			curr = nlist[i]
	return count
	

left, right = 0, len(nset)
maxlen = 0
while left <= right : 
	mid = (left + right) // 2

	# 해당 좌표로 수열 만들기
	count = 0
	for i, nl in enumerate(nlist) : 
		if nset[mid] == nl : 
			temp = getlen(i)
			# print("시작값 , 길이 : ", nl, temp)
			if count < temp :
				count = temp

	# 크네
	if count > maxlen : 
		right = mid - 1
		maxlen = count
	else : 
		left = mid + 1

print(maxlen)
	