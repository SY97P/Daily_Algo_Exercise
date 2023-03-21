from collections import Counter
from itertools import combinations
def solution(orders, course) :
	answer = []

	for c in course : 
		temp = []
		for order in orders : 
			combi = combinations(sorted(order), c)
			temp += combi
		counter = Counter(temp)
		if len(counter) != 0 and max(counter.values()) != 1 :
			answer += [''.join(menu) for menu in counter if counter[menu] == max(counter.values())]
	return sorted(answer)
						  
def main() : 
	orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]			# ["AC", "ACDE", "BCFG", "CDE"] 
	# orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]	
	# # ["ACD", "AD", "ADE", "CD", "XYZ"]
	# orders, course = ["XYZ", "XWY", "WXA"],	[2,3,4]	
	# # ["WX", "XY"]
	print("solution : ", solution(orders, course))

main()