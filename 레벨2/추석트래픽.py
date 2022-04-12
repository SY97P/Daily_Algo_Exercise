def solution(lines) : 
	answer = []
	log = []

	for l in lines : 
		_, end, time = l.split(" ")
		time = float(time[:len(time)-1])
		hour, min, sec = end.split(":")
		hour, min, sec = int(hour), int(min), float(sec)
		end = hour * 60 * 60 + min * 60 + sec 
		# print(end, time)

		# get start time 
		start = end - time + 0.001
		# print(start)

		log.append([start, end])

	# start와 end 기준으로 1초 차이 밖에 안 나면 count를 올림
	for l1 in log : 
		count = 0
		s1, e1 = l1
		for l2 in log : 
			print(l1, l2)
			s2, e2 = l2
			# start - start
			# print(round(abs(s1 - s2) + 0.001, 3))
			# print(round(abs(s1 - e2) + 0.001, 3))
			# print(abs(s2 - e1) + 0.001)
			# print(abs(e1 - e2) + 0.001)
			
			if round(abs(s1 - s2) + 0.001,3) <= 1 : 
				count += 1
				print("s1 - s2")
			# start - end
			elif round(abs(s1 - e2) + 0.001,3) <= 1 : 
				count += 1
				print("s1 - e2")
			# start - end
			elif round(abs(s2 - e1) + 0.001, 3) <= 1 :
				count += 1
				print("s2 - e1")
			# end - end
			elif round(abs(e1 - e2) + 0.001, 3) <= 1: 
				count += 1
				print("e1 - e2")
		print(count)
		answer.append(count)
	return max(answer)

def main() : 
	lines = ["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"] # 1
	lines = ["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"] # 2
	lines = [
		"2016-09-15 20:59:57.421 0.351s",
		"2016-09-15 20:59:58.233 1.181s",
		"2016-09-15 20:59:58.299 0.8s",
		"2016-09-15 20:59:58.688 1.041s",
		"2016-09-15 20:59:59.591 1.412s",
		"2016-09-15 21:00:00.464 1.466s",
		"2016-09-15 21:00:00.741 1.581s",
		"2016-09-15 21:00:00.748 2.31s",
		"2016-09-15 21:00:00.966 0.381s",
		"2016-09-15 21:00:02.066 2.62s"
	]			# 7
	print("solution : ", solution(lines))

main()

