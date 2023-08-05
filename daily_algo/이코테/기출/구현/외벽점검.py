n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
weak = [1,3,4,9,10]
dist = [3,5,7]

from itertools import permutations

length = len(weak)
for i in range(length):
	weak.append(weak[i] + n)
# print(weak)

answer = len(dist) + 1
for start in range(length):
	for friend in permutations(dist, len(dist)):
		count = 1
		position = weak[start] + friend[count-1]
		for index in range(start, start+length):
			if position < weak[index]:
				count += 1
				if count > len(dist):
					break
				position = weak[index] + friend[count - 1]
		answer = min(answer, count)
if answer > len(dist):
	print(-1)
else:
	print(answer)

# dist_list = list(permutations(dist, len(dist)))

# answer = 1e9
# for start in range(length):
# 	for case in dist_list:
# 		curr = weak[start]	
# 		weak_idx = start + 1
# 		count = 0
# 		for d in case:
# 			if weak_idx - start >= length:
# 				break
# 			while weak_idx < start + length and curr + d >= weak[weak_idx]:
# 				weak_idx += 1
# 			curr = weak[weak_idx]
# 			count += 1
# 		if curr >= weak[start+length]:
# 			answer = min(answer, count)

print(-1 if answer == 1e9 else answer)