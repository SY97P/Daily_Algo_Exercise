def solution(file) : 
	for _ in range(2) : 
		n = int(file.readline())
		cards = []
		for _ in range(n) : 
			cards.append(int(file.readline()))
		result = int(file.readline())
		cards.sort()

		if n < 2: 
			return cards.pop(0)
		elif n < 3: 
			return cards.pop(0) + cards.pop(0)
		else : 
			answer = cards.pop(0) + cards.pop(0)
			while cards : 
				answer += answer + cards.pop(0)
			return answer

# 백준 제출용
n = int(input())
cards = [int(input()) for _ in range(n)].sort()
if n < 2 : 
	print(cards.pop(0))
elif n < 3: 
	print(cards.pop(0) + cards.pop(0))
else : 
	answer = cards.pop(0) + cards.pop(0)
	while cards : 
		answer += answer + cards.pop(0)
	print(answer)


def main() : 
	file = open("./백준_그리디/카드정렬하기tc.txt", "r")

	print("solution : ", solution(file))
	
	file.close()

main()