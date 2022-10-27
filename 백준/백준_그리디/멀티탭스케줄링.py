def solution(file) :
	for tc in range(10) :
		try :
			print("TC : ", tc)
			n, k = map(int, file.readline().split())
			arr = list(map(int, file.readline().split()))
			answer = int(file.readline())
			file.readline()

			print(n, k, arr, answer)

			queue = [0] * n
			count = 0
			maxValue, maxIndex, num = 0, 0, 0

			for ar in arr :
				print("ar : ", ar, " queue :", queue)
				if ar in queue :
					print("ar is in queue")
					continue
				elif 0 in queue :
					print("queue has empty space")
					queue[queue.index(0)] = ar
					continue
				else :
					print("value of queue will be removed")
					for j in queue :
						if j not in arr[num:] :
							maxValue = j
							break
						elif maxIndex < arr[num:].index(j) :
							maxValue = j
							maxIndex = arr[num:].index(j)
					queue[queue.index(maxValue)] = ar
					maxValue, maxIndex = 0, 0
					count += 1
				num += 1
				
			print(count)
			print()
		except :
			print("Invalid Test Case Number")

# 백준 제출용
# import sys

# n, k = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))

# queue = [0] * n
# count = 0 
# maxValue, maxIndex, num = 0, 0, 0

# for ar in arr :
# 	if ar in queue :
# 		pass
# 	elif 0 in queue :
# 		queue[queue.index(0)] = ar
# 		pass
# 	else :
# 		for j in queue :
# 			if j not in arr[num:] :
# 				maxValue = j
# 				break
# 			elif maxIndex < arr[num:].index(j) :
# 				maxValue = j
# 				maxIndex = arr[num:].index(j)
# 		queue[queue.index(maxValue)] = ar
# 		maxValue, maxIndex = 0, 0
# 		count += 1
# 	num += 1

# print(count)

				

def main() :
	file = open("./백준_그리디/멀티탭스케줄링tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()

		