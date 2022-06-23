def solution(file) :
	for _ in range(1) :
		n, k = map(int, file.readline().split())
		arr = list(map(int, file.readline().split()))
		answer = int(file.readline())

		print(n, k, arr, answer)

		queue = [arr[i] for i in range(n)]
		count = 0

		for i in range(n, k) :
			if arr[i] in queue :
				continue
			else : 
				temp = []
				for j in range(n) :
					try :
						temp.append(arr[i+1:].index(queue[j]))
					except :
						temp.append(-1)
							
				print(temp)

				# temp에 -1(이제 안 씀)이 나오거나
				# temp에 가장 멀리서 쓰는 스케줄을 대체해줌
				isChanged = False
				if -1 in temp :
					queue[temp.index(-1)] = arr[i]
					isChanged = True
				if not isChanged :
					queue[temp.index(max(temp))] = arr[i]
					isChanged = True
				count += 1

		print(count)

# 백준 제출용
n, k = map(int, input().split())
arr = list(map(int, input().split()))
queue = [arr[i] for i in range(n)]
count = 0

for i in range(n, k) :
	if arr[i] in queue :
		continue
	temp = []
	for j in range(n) :
		try :
			temp.append(arr[i+1:].index(queue[j]))
		except :
			temp.append(-1)
	isChanged = False
	if -1 in temp :
		queue[temp.index(-1)] = arr[i]
		isChanged = True
	if not isChanged :
		queue[temp.index(max(temp))] = arr[i]
		isChanged = True
	count += 1

print(count)
				


def main() :
	file = open("./백준_그리디/멀티탭스케줄링tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()

		