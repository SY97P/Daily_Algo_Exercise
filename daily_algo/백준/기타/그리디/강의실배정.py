import heapq
def solution(file) :
	for _ in range(1) :
		n = int(file.readline())
		arr = [list(map(int, file.readline().split())) for i in range(n)]
		answer = int(file.readline())

		room_time = [arr[0][1]]

		print(n, arr, answer, room_time)

		for i in range(1, n) :
			# 현재 시작시간이 가장 빨리 끝나는 강의보다 빨리 시작하면
			# 방을 하나 더 줌
			if arr[i][0] < room_time[0] :
				heapq.heappush(room_time, arr[i][1])
			# 현재 시작시간이 가장 빨리 끝나는 강의보다 늦게 시작하면
			# 기존의 방을 제거하고 새로 넣어줌
			else :
				heapq.heappop(room_time)
				heapq.heappush(room_time, arr[i][1])

		print(len(room_time))

# 다 좋은데 입력값 받는게 input()이 아니라 sys.stdin.readline()으로 해야 했음
# 백준 제출용
# n = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# arr.sort()
# room_time = [arr[0][1]]

# for i in range(1, n) :
# 	start, end = arr[i]
# 	if start < room_time[0] :
# 		heapq.heappush(room_time, end)
# 	else :
# 		heapq.heappop(room_time)
# 		heapq.heappush(room_time, end)
# print(len(room_time))

def main() :
	file = open("./그리디/강의실배정tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
