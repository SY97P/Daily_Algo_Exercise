from collections import deque

def isProper(digit) : 
    q = deque([len(digit) // 2])
    length = len(digit)
	visited = [False for _ in range(length)]
	while q : 
        curr = q.popleft()

        print(curr, digit[curr])

        # 현재 노드가 더미 노드인데 리프 노드가 아니라면 False
        if digit[curr] != "0" :
            if curr - 2 >= 0 and curr + 2 < length : 
				if not visited[curr - 2] : 
                	q.append(curr - 2)
					visited[curr - 2] = True
				if not visited[curr + 2] : 
					visited[curr +2 ] = True
                	q.append(curr + 2)
            elif curr - 1 >= 0 and curr + 1 < length : 
				if not visited[curr - 1] : 
					visited[curr -1] = True
                	q.append(curr - 1)
				if not visited[curr + 1] : 
					visited[curr + 1] = True
                	q.append(curr + 1)
        else : 
            # print("bound")
            if curr - 2 >= 0 and curr + 2 < length : 
                # print("2 bound")
                return False
            elif curr - 1 >= 0 and curr + 1 < length : 
                # print("1 bound")
                return False

    return True

def digify(num) : 
    result = ""
    while num >= 2: 
        result = str(num % 2) + result
        num //= 2
    if num != 0 :
        result = str(num) + result
    if len(result) % 2 == 0 : 
        result = "0" + result
    return result

def solution(numbers):
    answer = []

    for num in numbers : 
        digit = digify(int(num))
        print(digit)
        if isProper(digit) :
            answer.append(1)
        else: 
            answer.append(0)

    return answer

def main() : 
	numbers = [63, 111, 95]
	print(solution(numbers))

main()