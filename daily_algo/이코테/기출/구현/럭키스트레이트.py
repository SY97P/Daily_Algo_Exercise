number = list(map(int, input().strip()))

if sum(number[:len(number)//2]) == sum(number[len(number)//2:]):
	print("LUCKY")
else:
	print("READY")