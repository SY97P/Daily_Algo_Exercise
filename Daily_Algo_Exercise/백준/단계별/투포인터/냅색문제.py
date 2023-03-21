# 3
# 2
# 2
# 1
# 4
# 1073741824

file = open("./백준/투포인터/냅색문제.txt", "r")

input = file.readline

from itertools import combinations

# for _ in range(6) :
n, c = map(int, input().split())
weights = list(map(int, input().split()))

# print(n, c)
# print(weights)

bound = n//2 if not n%2 else n//2+1
a, b = weights[:bound], weights[bound:]
len_a, len_b = len(a), len(b)
sub_a, sub_b = [], []

for i in range(len_a+1) : 
	for combi in combinations(a, i) : 
		sub_a.append(sum(combi))

for i in range(len_b+1) : 
	for combi in combinations(b, i) : 
		sub_b.append(sum(combi))

# print(sub_a)
# print(sub_b)

sub_b.sort()

count = 0

for sumof in sub_a : 
	if sumof > c :
		continue

	left, right = 0, len(sub_b)

	while left < right : 
		mid = (left + right) // 2

		if sumof + sub_b[mid] > c : 
			right = mid
		else : 
			left = mid + 1

	count += right

print(count)

file.close()