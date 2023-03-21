#1 SOFTWARE
#2 COMPUTER_SCIENCE_AND_ENGINEERING
#3 SOFWARE_ALGORITHM_AND_DATA_STRUCT
#4 DEPTH_FIRST_SEARCH_AND_BREATH_FIRST_SEARCH
#5 WELCOME_TO_ALGORITHM_PROBLEM_SOLVING
#6 ARRAY_STRING_STACK_QUEUE_TREE_GRAPH
#7 HE_WHO_WOULD_HAVE_THE_KERNEL_MUST_CRACK_THE_SHELL
#8 THE_PRESENT_IS_THE_PRESENT_MOMENT
#9 IN_ORDER_PRE_ORDER_POST_ORDER_TRACE
#10 TECHNOLOGY_TRAINING_INSTITUTE

file = open("./SWEA/D4/중위순회.txt", "r")

input = file.readline

# from collections import defaultdict

def dfs(node) : 
	global result

	info = dic[node]

	if len(info) < 3: # leaf
		result += info[1]
		return
	elif len(info) < 4 : 
		dfs(info[2])
		result += info[1]
	else : 
		dfs(info[2])
		result += info[1]
		dfs(info[3])
	

for tc in range(1, 11) : 
	dic = dict()
	
	n = int(input())
	
	for _ in range(n) : 
		info = input().split()

		# leaf
		if len(info) < 3 : 
			dic[int(info[0])] = (int(info[0]), info[1])
		# one child node (left node only)
		elif len(info) < 4 : 
			dic[int(info[0])] = (int(info[0]), info[1], int(info[2]))
		# two child node (both node exist)
		else : 
			dic[int(info[0])] = (int(info[0]), info[1], int(info[2]),  int(info[3]))
		
	result = ""

	dfs(1)

	print("#%d %s" %(tc, result))

file.close()