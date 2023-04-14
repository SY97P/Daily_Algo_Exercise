from bisect import bisect_left, bisect_right

def get_count(data, left_key, right_key):
	left_bound = bisect_left(data, left_key)
	right_bound = bisect_right(data, right_key)
	return right_bound - left_bound

def solution(words, queries):
	for_data = dict()
	rev_data = dict()
	for word in words:
		if len(word) in for_data:
			for_data[len(word)].append(word)
			rev_data[len(word)].append(word[::-1])
		else:
			for_data[len(word)] = [word]
			rev_data[len(word)] = [word[::-1]]

	for key in for_data.keys():
		for_data[key].sort()
		rev_data[key].sort()

	answer = []

	for q in queries:
		if len(q) not in for_data:
			answer.append(0)
			continue 
		if q[-1] == "?":
			answer.append(get_count(for_data[len(q)], q.replace('?', 'a'), q.replace('?', 'z')))
		elif q[0] == "?":
			answer.append(get_count(rev_data[len(q)], q.replace('?', 'a')[::-1], q.replace('?', 'z')[::-1]))

	return answer


def main():
	words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
	queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
	print(solution(words, queries))

main()