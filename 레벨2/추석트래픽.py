# def solution(lines) :
# 	answer = []
# 	log = []

# 	for l in lines : 
# 		_, end, time = l.split(" ")
# 		print("befor : ", end, time)
# 		hour, min, sec = end.split(":")
		
# 		# 60초 넘을 경우 -> 타임아웃이 3초로 주어짐.
# 		# time = float(time[:len(time)-1])
# 		# while time >= 60.0 : 
# 		# 	min -= 1
# 		# 	time -= 60.0

# 		# 58:01.34 - 2.08 = 57:(60.0 + 01.34 - 2.08)
# 		time = float(time[:len(time)-1])
# 		print("sec : ", sec, "time : ", time)
# 		sec = str("{:.3f}".format(float(sec) - time + 0.001))
# 		if float(sec) < 0 : 
# 			sec = str("{:.3f}".format(float(sec) + 60))
# 			min = str(int(min) - 1)
# 		if int(min) < 0 : 
# 			min = str(int(min) + 60)
# 			hour = str(int(hour) - 1)
# 		start = hour + ":" + min + ":" + sec
# 		print(start)

# 		log.append([start, end])

# 	print(log)

# 	temp = []
# 	start, end = log[0]
# 	for l in log : 
# 		if start < l[0] : 
# 			start = l[0]
# 		if end > l[1] : 
# 			end = l[1]
# 		print(start, end)
# 		isCorrect(start, end)

# def isCorrect(start, end) : 
# 	shour, smin, ssec = start.split(":")
# 	ehour, emin, esec = end.split(":")
# 	if min(shour) < min(ehour)
	
		

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

