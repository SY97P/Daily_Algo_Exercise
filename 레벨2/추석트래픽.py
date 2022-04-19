def solution(lines) : 
	answer = []
	log = []

	for l in lines : 
		_, end, time = l.split(" ")
		end = getTime(end)
		# print(end)
		time = int(float(time[:len(time)-1]) * 1000)
		start = getStart(end, time)
		# print(start, end)
		log.append([start, end])

	for i in range(len(log)) : 
		count = 0 
		i_start, i_end = log[i]
		for j in range(i, len(log)) : 
			j_start, j_end = log[j]
			# print(i_start, i_end, j_start, j_end)

		# 현재 마지막 시간과 다음 시작 시간 차이가 1000 이하면 된다고 함. 
			# print("분기 : ", j_start, i_end + 1000 - 1)
			if j_start < i_end + 1000 + 1 : 
				count += 1
		answer.append(count)
	# print(answer)
	return max(answer)

def getTime(end) : 
	return int(end[:2]) * 60 * 60 * 1000 + int(end[3:5]) * 60 * 1000 + int(float(end[6:]) * 1000)

def getStart(end, time) : 
	return end - time + 2
	

def main() : 
	lines = ["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"] # 1
	# lines = ["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"] # 2
	# lines = [
	# 	"2016-09-15 20:59:57.421 0.351s",
	# 	"2016-09-15 20:59:58.233 1.181s",
	# 	"2016-09-15 20:59:58.299 0.8s",
	# 	"2016-09-15 20:59:58.688 1.041s",
	# 	"2016-09-15 20:59:59.591 1.412s",
	# 	"2016-09-15 21:00:00.464 1.466s",
	# 	"2016-09-15 21:00:00.741 1.581s",
	# 	"2016-09-15 21:00:00.748 2.31s",
	# 	"2016-09-15 21:00:00.966 0.381s",
	# 	"2016-09-15 21:00:02.066 2.62s"
	# ]			# 7
	# lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"] # 2
	print("solution : ", solution(lines))

main()

