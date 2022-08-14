file = open("./이진탐색/공유기설치tc.txt", "r")

n, c = map(int, file.readline().split())
houses = [int(file.readline()) for _ in range(n)]
answer = int(file.readline())

print(n, c, answer)
print(houses)

houses.sort()

left, right = 1, houses[-1]-houses[0]
while left <= right : 
	mid = (left + right) //2

	


file.close()