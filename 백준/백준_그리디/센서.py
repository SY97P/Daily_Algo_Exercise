file = open("./백준_그리디/센서tc.txt", "r")

read = file.readline

for _ in range(2) :
	n = int(read())
	k = int(read())
	sensors = list(map(int, read().split()))
	answer = int(read())
	read()
	
	print(n, k, sensors, answer)

	sensors.sort()

	# print(sensors)

	# 각 센서 사이 거리를 구함
	distances = [sensors[i] - sensors[i-1] for i in range(1, n)]
	# print(distances)

	# 센서끼리 거리 중 k - 1개만 제거하면 됨
	distances.sort()

	# print(distances[:len(distances) - (k-1)])

	print(sum(distances[:len(distances) - (k-1)]))
	print()

file.close()

# 백준 제출용
n = int(input())
k = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

distances = [sensors[i] - sensors[i-1] for i in range(1, n)]
distances.sort()

print(sum(distances[:len(distances) - (k-1)]))