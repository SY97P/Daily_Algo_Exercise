def solution(n, stages):
	failure = []
	total = len(stages)
	for score in range(1, n+1):
		count = stages.count(score)
		fail = count / total 
		total -= count
		failure.append((fail, score))
	failure.sort(key=lambda x: -x[0])
	answer = []
	for f, s in failure:
		answer.append(s)
	return answer


def main():
	n = 5
	stages = [2,1,2,6,2,4,3,3]
	print(solution(n, stages))

main()