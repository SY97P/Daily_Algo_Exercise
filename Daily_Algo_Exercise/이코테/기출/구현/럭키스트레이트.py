number = input().strip()

left = list(map(int, number[:len(number)//2]))
right = list(map(int, number[len(number)//2:]))

if sum(left) == sum(right):
	print("LUCKY")
else:
	print("READY")