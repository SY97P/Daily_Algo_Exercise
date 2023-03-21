#1 Bob
#2 Alice
#3 Bob
#4 Alice
#5 Bob

file = open("./SWEA/D4/승자예측하기.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	n = int(input())

	key = False

	# print(n)

	n //= 2
	n += 1
	
	while n > 1 : 
		if key : 
			n = (n+1)//2
		else : 
			n = n // 2

		key = False if key else True

	print("#%d %s" %(tc, "Alice" if key else "Bob"))


file.close()