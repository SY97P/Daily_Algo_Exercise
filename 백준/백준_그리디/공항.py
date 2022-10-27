file = open("./백준_그리디/공항tc.txt", "r")

def union(curr_index, prev_index) : 
	print(curr_index, prev_index)
	curr = parent(curr_index)
	prev = parent(prev_index)
	print(curr, prev)
	# 낮은 급수의 공항이 더 수용량이 많으면 낮은 급수의 수용량을 현재 수용량으로 맞춰줌 (이미 현재 공항에는 한 대가 온 상황이므로 전 공항 수용량과 같아야 함)
	if curr < prev : 
		gates[prev] = curr
	elif curr > prev :
		gates[curr] = prev
	else :
		union(curr_index - 1, prev_index)

def parent(item) : 
	if item != gates[item] :
		gates[item] = parent(gates[item])
	return gates[item]

for tc in range(4) :
	g = int(file.readline())
	p = int(file.readline())
	planes = [int(file.readline()) for _ in range(p)]
	answer = int(file.readline())
	file.readline()

	print(g, p, " / ", answer)
	print(planes)

	gates = {i : i for i in range(g+1)}

	step = 0

	for plane in planes : 
		if parent(plane) == 0 :
			break
		print(gates)
		union(plane, plane - 1)
		step += 1

	print(step)
	print()

file.close()

# 백준 제출용
