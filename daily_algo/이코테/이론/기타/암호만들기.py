from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())
tokens = list(input().strip().split())
tokens.sort()

answer = []
for x in combinations(tokens, l):
	count = 0
	for i in x:
		if i in vowels:
			count += 1
	if 1 <= count <= l - 2:
		answer.append(''.join(list(x)))
answer.sort()

for a in answer:
	print(a)