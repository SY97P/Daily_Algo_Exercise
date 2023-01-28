def solution(n, time) : 
	answer =  0
	curr = 0
	for t in sorted(time) : 
		curr += t
		answer += curr
	return answer
    
def main() : 
    n, time = 5, [3, 1, 4, 3, 2]
    print("solution : ", solution(n, time))
    
main()