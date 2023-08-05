n = int(input())

ugly = [0] * (n*2)
ugly[1] = 1

for i in range(2, n*2):
	if i%2 == 0 and ugly[i//2] == 1:
		ugly[i] = 1
	if i%3 == 0 and ugly[i//3] == 1:
		ugly[i] = 1
	if i%5 == 0 and ugly[i//5] == 1:
		ugly[i] = 1

answer = 1
idx = 0
for i in range(1, n*2):
	if ugly[i] == 1:
		idx += 1
	if idx == n:
		answer = i
		break
print(answer)