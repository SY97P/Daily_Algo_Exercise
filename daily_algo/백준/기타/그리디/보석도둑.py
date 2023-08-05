import heapq
def solution(file) : 
	for _ in range(2) :
		n, k = list(map(int, file.readline().split()))
		jewel, bag = [], []
		for _ in range(n) : 
			jewel.append(list(map(int, file.readline().split())))
		for _ in range(k) : 
			bag.append(int(file.readline()))
		answer = int(file.readline())

		print(n, k, jewel, bag, answer)

		jewel.sort()
		bag.sort()

		result = 0
		temp = []
		heapq.heapify(temp)
		heapq.heapify(jewel)
		
		for b in bag : 
			while jewel and b >= jewel[0][0] :
				heapq.heappush(temp, -jewel[0][1])
				heapq.heappop(jewel)

			if temp :
				result += heapq.heappop(temp)
			elif not jewel :
				break

		print(-result)
	

def main() : 
	file = open("./그리디/보석도둑tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()
